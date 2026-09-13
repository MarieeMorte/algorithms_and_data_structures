from __future__ import annotations

import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

LAB_DIR = REPO_ROOT / "src" / "lab4"

NAMED_TASKS = {
    "text_shift": "text_shift.py",
    "substring_search": "substring_search.py",
    "cyclic_string": "cyclic_string.py",
}


def solution_path(task) -> Path:
    if isinstance(task, int):
        candidate = LAB_DIR / f"task{task}.py"
        if candidate.exists():
            return candidate
        alt = LAB_DIR / f"task{task}" / f"task{task}.py"
        if alt.exists():
            return alt
        raise FileNotFoundError(
            f"Не найден файл решения для task{task}. Ожидался: {candidate}"
        )

    if isinstance(task, str):
        if task not in NAMED_TASKS:
            raise KeyError(
                f"Неизвестное имя задачи: {task!r}. "
                f"Доступные: {sorted(NAMED_TASKS)}"
            )
        candidate = LAB_DIR / NAMED_TASKS[task]
        if not candidate.exists():
            raise FileNotFoundError(
                f"Не найден файл решения для {task!r}. Ожидался: {candidate}"
            )
        return candidate

    raise TypeError(
        f"task должен быть int или str, получено: {type(task).__name__}"
    )


_WRAPPER = """\
import platform, runpy, sys


def get_peak_memory_bytes():
    system = platform.system()

    if system == "Windows":
        try:
            import ctypes
            from ctypes import wintypes

            class PROCESS_MEMORY_COUNTERS(ctypes.Structure):
                _fields_ = [
                    ("cb", wintypes.DWORD),
                    ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t),
                    ("PeakPagefileUsage", ctypes.c_size_t),
                ]

            counters = PROCESS_MEMORY_COUNTERS()
            counters.cb = ctypes.sizeof(counters)
            handle = ctypes.windll.kernel32.GetCurrentProcess()

            ok = 0
            for dll_name, fn_name in (
                ("kernel32", "K32GetProcessMemoryInfo"),
                ("psapi", "GetProcessMemoryInfo"),
            ):
                try:
                    dll = ctypes.WinDLL(dll_name)
                    fn = getattr(dll, fn_name, None)
                    if fn is None:
                        continue
                    fn.restype = wintypes.BOOL
                    fn.argtypes = [
                        wintypes.HANDLE,
                        ctypes.POINTER(PROCESS_MEMORY_COUNTERS),
                        wintypes.DWORD,
                    ]
                    ok = fn(handle, ctypes.byref(counters), counters.cb)
                    if ok:
                        break
                except (OSError, AttributeError):
                    continue

            if not ok:
                return 0
            return int(counters.PeakWorkingSetSize)
        except Exception:
            return 0

    import resource
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if system == "Darwin":
        return int(mem)
    return int(mem) * 1024


runpy.run_path(sys.argv[1], run_name="__main__")

mem_bytes = get_peak_memory_bytes()
with open(sys.argv[2], "w") as f:
    f.write(str(mem_bytes))
"""

_BASELINE_BYTES: int | None = None


def _format_bytes(n: int) -> str:
    if n <= 0:
        return "0 B"
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024
    return f"{n:.1f} GB"


def _measure_baseline_bytes() -> int:
    global _BASELINE_BYTES
    if _BASELINE_BYTES is not None:
        return _BASELINE_BYTES

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "empty.py").write_text("", encoding="utf-8")
        (tmp / "wrapper.py").write_text(_WRAPPER, encoding="utf-8")

        subprocess.run(
            [sys.executable, str(tmp / "wrapper.py"),
             str(tmp / "empty.py"), str(tmp / "mem.txt")],
            cwd=tmp, capture_output=True, text=True, timeout=30,
        )
        mem_file = tmp / "mem.txt"
        _BASELINE_BYTES = (
            int(mem_file.read_text().strip()) if mem_file.exists() else 0
        )

    return _BASELINE_BYTES


def run_task(task, input_data: str, timeout: float = 30):
    """
    task: int (номер) или str (имя задачи, например "text_shift")
    :return: (output_text, elapsed_seconds, net_peak_memory_bytes)
    """
    task_path = solution_path(task).resolve()

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "input.txt").write_text(input_data, encoding="utf-8")
        (tmp / "wrapper.py").write_text(_WRAPPER, encoding="utf-8")

        start = time.perf_counter()
        proc = subprocess.run(
            [sys.executable, str(tmp / "wrapper.py"),
             str(task_path), str(tmp / "mem.txt")],
            cwd=tmp, capture_output=True, text=True, timeout=timeout,
        )
        elapsed = time.perf_counter() - start

        if proc.returncode != 0:
            raise AssertionError(
                f"Решение {task_path} упало с кодом {proc.returncode}\n"
                f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
            )

        out_file = tmp / "output.txt"
        output = (
            out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        )

        mem_file = tmp / "mem.txt"
        mem_bytes = (
            int(mem_file.read_text().strip()) if mem_file.exists() else 0
        )

    baseline = _measure_baseline_bytes()
    net_bytes = max(0, mem_bytes - baseline)

    return output.strip(), elapsed, net_bytes


def check(task, input_data: str, expected: str | None = None,
          timeout: float = 30) -> str:
    output, elapsed, mem_bytes = run_task(task, input_data, timeout=timeout)

    total = mem_bytes + _measure_baseline_bytes()
    label = task if isinstance(task, str) else f"task{task}"
    print(f"\n[{label}] time={elapsed:.3f}s  "
          f"memory={_format_bytes(mem_bytes)} (net), "
          f"{_format_bytes(total)} (total)")

    preview = output if len(output) <= 200 else output[:200] + "..."
    print(f"  output: {preview}")

    if expected is not None:
        assert output == expected, (
            f"\nОжидалось:\n{expected!r}\n\nПолучено:\n{output!r}"
        )
    return output
