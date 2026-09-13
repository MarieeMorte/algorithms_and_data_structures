import bisect
import random

from test_utils import check


def test_minimal():
    check(16, "2\n+1 5\n0 1\n", "5")


def test_example():
    check(
        16,
        "11\n"
        "+1 5\n"
        "+1 3\n"
        "+1 7\n"
        "0 1\n"
        "0 2\n"
        "0 3\n"
        "-1 5\n"
        "+1 10\n"
        "0 1\n"
        "0 2\n"
        "0 3\n",
        "7\n5\n3\n10\n7\n3",
    )


def test_maximum():
    n = 100_000
    half = n // 2
    lines = [str(n)]
    for i in range(1, half + 1):
        lines.append(f"+1 {i}")
    expected = []
    for k in range(1, half + 1):
        lines.append(f"0 {k}")
        expected.append(str(half - k + 1))
    input_data = "\n".join(lines) + "\n"
    check(16, input_data, "\n".join(expected), timeout=60)


def test_single_element_query():
    check(16, "3\n+1 42\n0 1\n-1 42\n", "42")


def test_negative_keys():
    check(
        16,
        "7\n"
        "+1 -5\n"
        "+1 -1\n"
        "+1 -10\n"
        "0 1\n"
        "0 2\n"
        "0 3\n"
        "0 3\n",
        "-1\n-5\n-10\n-10",
    )


def test_k_equals_one_is_max():
    check(
        16,
        "5\n"
        "+1 3\n"
        "+1 1\n"
        "+1 2\n"
        "0 1\n"
        "0 3\n",
        "3\n1",
    )


def test_delete_then_query():
    check(
        16,
        "8\n"
        "+1 1\n"
        "+1 2\n"
        "+1 3\n"
        "0 1\n"
        "-1 3\n"
        "0 1\n"
        "-1 1\n"
        "0 1\n",
        "3\n2\n2",
    )


def test_add_delete_add():
    check(
        16,
        "8\n"
        "+1 5\n"
        "-1 5\n"
        "+1 10\n"
        "+1 20\n"
        "0 1\n"
        "0 2\n"
        "-1 20\n"
        "0 1\n",
        "20\n10\n10",
    )


def test_max_key_values():
    check(
        16,
        "8\n"
        "+1 1000000000\n"
        "+1 -1000000000\n"
        "+1 0\n"
        "0 1\n"
        "0 2\n"
        "0 3\n"
        "-1 1000000000\n"
        "0 1\n",
        "1000000000\n0\n-1000000000\n0",
    )


def test_maximum_with_deletions():
    n_elems = 30000
    n_queries = 30000
    n_dels = 15000
    n_queries2 = 15000
    total = n_elems + n_queries + n_dels + n_queries2
    lines = [str(total)]
    for i in range(1, n_elems + 1):
        lines.append(f"+1 {i}")
    expected = []
    for k in range(1, n_queries + 1):
        lines.append(f"0 {k}")
        expected.append(str(n_elems - k + 1))
    for i in range(1, n_dels + 1):
        lines.append(f"-1 {i}")
    for k in range(1, n_queries2 + 1):
        lines.append(f"0 {k}")
        expected.append(str(n_elems - k + 1))
    input_data = "\n".join(lines) + "\n"
    check(16, input_data, "\n".join(expected), timeout=60)


def test_random_interleaved():
    random.seed(16)
    n = 5000
    lines = [str(n)]
    arr = []
    expected = []
    key_counter = 0
    for _ in range(n):
        r = random.random()
        if not arr or r < 0.6:
            lines.append(f"+1 {key_counter}")
            bisect.insort(arr, key_counter)
            key_counter += 1
        elif r < 0.8:
            k = random.randint(1, len(arr))
            lines.append(f"0 {k}")
            expected.append(str(arr[-k]))
        else:
            idx = random.randint(0, len(arr) - 1)
            val = arr.pop(idx)
            lines.append(f"-1 {val}")
    input_data = "\n".join(lines) + "\n"
    check(16, input_data, "\n".join(expected), timeout=60)
