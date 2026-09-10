import itertools
import random

from test_utils import check


def test_minimal():
    check(13, "1\n3\n", "0")


def test_example_1():
    check(13, "4\n3 3 3 3\n", "0")


def test_example_2():
    check(13, "1\n40\n", "0")


def test_example_3():
    check(13, "11\n17 59 34 57 17 23 67 1 18 2 59\n", "1")


def test_example_4():
    check(13, "13\n1 2 3 4 5 5 7 7 8 10 12 19 25\n", "1")


def test_maximal_yes():
    n = 18
    values = " ".join(["10"] * n)
    check(13, f"{n}\n{values}\n", "1")


def test_maximal_no():
    n = 20
    values = " ".join(["30"] * n)
    check(13, f"{n}\n{values}\n", "0")


def test_minimal_three_equal():
    check(13, "3\n1 1 1\n", "1")


def test_two_items():
    check(13, "2\n1 2\n", "0")


def test_sum_not_divisible():
    check(13, "3\n1 2 4\n", "0")


def test_one_too_big():
    check(13, "3\n100 1 1\n", "0")


def test_all_equal_six():
    check(13, "6\n10 10 10 10 10 10\n", "1")


def test_all_equal_five():
    check(13, "5\n3 3 3 3 3\n", "0")


def test_sum_ok_but_no_partition():
    check(13, "4\n1 1 1 3\n", "0")


def test_exact_split():
    check(13, "6\n1 1 1 1 1 1\n", "1")


def test_mixed():
    check(13, "6\n1 2 3 1 2 3\n", "1")


def test_three_equal_groups():
    check(13, "6\n4 4 4 4 4 4\n", "1")


def _brute_force(values):
    total = sum(values)
    if total % 3 != 0:
        return 0
    target = total // 3
    n = len(values)
    for assign in itertools.product(range(3), repeat=n):
        sums = [0, 0, 0]
        for i, g in enumerate(assign):
            sums[g] += values[i]
        if sums[0] == sums[1] == sums[2] == target:
            return 1
    return 0


def test_stress_random_small():
    random.seed(13)
    for trial in range(30):
        n = random.randint(3, 8)
        values = [random.randint(1, 10) for _ in range(n)]

        input_data = f"{n}\n" + " ".join(map(str, values)) + "\n"

        expected = _brute_force(values)
        got = int(check(13, input_data))

        assert got == expected, (
            f"trial #{trial}: values={values}\n"
            f"expected={expected}, got={got}"
        )
