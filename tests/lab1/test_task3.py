import itertools
import random

from test_utils import check


def test_minimal():
    check(3, "1\n5\n7\n", "35")


def test_example_1():
    check(3, "1\n23\n39\n", "897")


def test_example_2():
    check(3, "3\n1 3 -5\n-2 4 1\n", "23")


def test_maximal():
    n = 1000
    a = " ".join(["100000"] * n)
    b = " ".join(["100000"] * n)
    expected = str(100000 * 100000 * n)
    check(3, f"{n}\n{a}\n{b}\n", expected)


def test_all_zeros():
    check(3, "3\n0 0 0\n0 0 0\n", "0")


def test_one_side_zeros():
    check(3, "3\n1 2 3\n0 0 0\n", "0")


def test_all_negative():
    check(3, "3\n-1 -2 -3\n-4 -5 -6\n", "32")


def test_mixed_signs():
    check(3, "3\n-5 1 3\n-2 1 4\n", "23")


def test_one_positive_one_negative_side():
    check(3, "3\n-1 -2 -3\n1 2 3\n", "-10")


def test_single_positive_single_negative():
    check(3, "1\n-5\n10\n", "-50")


def test_same_elements():
    check(3, "3\n2 2 2\n3 3 3\n", "18")


def test_two_elements_sorted():
    check(3, "2\n1 2\n3 4\n", "11")


def test_two_elements_reverse_sorted():
    check(3, "2\n2 1\n4 3\n", "11")


def test_trap_naive_pairing():
    check(3, "2\n10 1\n1 10\n", "101")


def test_large_values_mixed():
    check(3, "3\n100000 -100000 100000\n100000 100000 -100000\n", "30000000000")


def test_boundary_values():
    check(3, "2\n-100000 100000\n-100000 100000\n", "20000000000")


def _brute_force(a, b):
    best = None
    for perm in itertools.permutations(b):
        total = sum(x * y for x, y in zip(a, perm))
        if best is None or total > best:
            best = total
    return best


def test_stress_random_small():
    random.seed(42)
    for trial in range(30):
        n = random.randint(1, 6)
        a = [random.randint(-20, 20) for _ in range(n)]
        b = [random.randint(-20, 20) for _ in range(n)]

        input_data = (
                f"{n}\n"
                + " ".join(map(str, a)) + "\n"
                + " ".join(map(str, b)) + "\n"
        )

        expected = _brute_force(a, b)
        got = int(check(3, input_data))

        assert got == expected, (
            f"trial #{trial}: a={a}, b={b}\n"
            f"expected={expected}, got={got}"
        )
