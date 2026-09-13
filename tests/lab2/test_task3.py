import bisect
import random

from test_utils import check


def test_minimal():
    check(3, "+ 1\n", "")


def test_example():
    check(
        3,
        "+ 1\n"
        "+ 3\n"
        "+ 3\n"
        "> 1\n"
        "> 2\n"
        "> 3\n"
        "+ 2\n"
        "> 1\n",
        "3\n3\n0\n2",
    )


def test_maximum():
    random.seed(42)
    n = 300_000
    lines = []
    added = set()

    for _ in range(n // 2):
        x = random.randint(1, 10 ** 9)
        if x not in added:
            added.add(x)
            lines.append(f"+ {x}")

    for _ in range(n - len(lines)):
        x = random.randint(0, 10 ** 9)
        lines.append(f"> {x}")

    input_data = "\n".join(lines) + "\n"

    sorted_vals = sorted(added)
    expected = []
    for line in lines:
        if line.startswith(">"):
            x = int(line[2:])
            idx = bisect.bisect_right(sorted_vals, x)
            if idx < len(sorted_vals):
                expected.append(str(sorted_vals[idx]))
            else:
                expected.append("0")

    check(3, input_data, "\n".join(expected), timeout=60)


def test_minimal_add_and_query():
    check(3, "+ 5\n> 4\n", "5")


def test_query_empty_tree():
    check(3, "> 5\n", "0")


def test_query_no_greater():
    check(3, "+ 1\n+ 2\n+ 3\n> 3\n", "0")


def test_query_all_greater():
    check(3, "+ 10\n+ 20\n+ 30\n> 5\n", "10")


def test_duplicates_ignored():
    check(3, "+ 5\n+ 5\n+ 5\n> 4\n> 5\n", "5\n0")


def test_single_element_max_key():
    check(3, "+ 1000000000\n> 999999999\n> 1000000000\n", "1000000000\n0")


def test_min_key():
    check(3, "+ 1\n> 0\n> 1\n", "1\n0")


def test_query_zero():
    check(3, "+ 5\n+ 10\n> 0\n", "5")


def test_ascending_insertion():
    lines = []
    for i in range(1, 101):
        lines.append(f"+ {i}")
    lines.append("> 50")
    lines.append("> 100")
    lines.append("> 0")
    check(3, "\n".join(lines) + "\n", "51\n0\n1")


def test_descending_insertion():
    lines = []
    for i in range(100, 0, -1):
        lines.append(f"+ {i}")
    lines.append("> 50")
    lines.append("> 99")
    lines.append("> 0")
    check(3, "\n".join(lines) + "\n", "51\n100\n1")


def test_maximum_interleaved():
    random.seed(123)
    n = 30_000
    lines = []
    sorted_vals = []
    expected = []

    for _ in range(n):
        if random.random() < 0.5:
            x = random.randint(1, 10 ** 9)
            lines.append(f"+ {x}")
            if x not in sorted_vals:
                bisect.insort(sorted_vals, x)
        else:
            x = random.randint(0, 10 ** 9)
            lines.append(f"> {x}")
            idx = bisect.bisect_right(sorted_vals, x)
            if idx < len(sorted_vals):
                expected.append(str(sorted_vals[idx]))
            else:
                expected.append("0")

    input_data = "\n".join(lines) + "\n"
    check(3, input_data, "\n".join(expected), timeout=60)
