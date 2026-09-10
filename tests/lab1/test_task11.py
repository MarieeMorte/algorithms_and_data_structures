import random

from test_utils import check


def test_minimal():
    check(11, "1 1\n1\n", "1")


def test_example():
    check(11, "10 3\n1 4 8\n", "9")


def test_maximal():
    n = 300
    w = 10000
    weights = " ".join(["100"] * n)
    check(11, f"{w} {n}\n{weights}\n", "10000")


def test_maximal_all_too_heavy():
    n = 300
    w = 10000
    weights = " ".join(["100000"] * n)
    check(11, f"{w} {n}\n{weights}\n", "0")


def test_single_item_too_heavy():
    check(11, "5 1\n10\n", "0")


def test_single_item_exact():
    check(11, "7 1\n7\n", "7")


def test_zero_weight_items():
    check(11, "5 3\n0 0 0\n", "0")


def test_zero_weight_and_positive():
    check(11, "5 2\n0 5\n", "5")


def test_two_items_both_fit():
    check(11, "10 2\n4 5\n", "9")


def test_two_items_pick_heavier():
    check(11, "10 2\n7 9\n", "9")


def test_all_weights_equal():
    check(11, "10 5\n3 3 3 3 3\n", "9")


def test_greedy_by_weight_fails():
    check(11, "10 3\n8 5 5\n", "10")


def test_subset_sum_exact():
    check(11, "15 4\n4 5 6 7\n", "15")


def test_dp_classic():
    check(11, "10 3\n1 4 8\n", "9")


def test_all_equal_exact_fit():
    check(11, "20 4\n5 5 5 5\n", "20")


def test_w_one():
    check(11, "1 3\n1 2 3\n", "1")


def _brute_force(weights, w):
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        total = 0
        ok = True
        for i in range(n):
            if mask & (1 << i):
                total += weights[i]
                if total > w:
                    ok = False
                    break
        if ok and total > best:
            best = total
    return best


def test_stress_random_small():
    random.seed(777)
    for trial in range(30):
        n = random.randint(1, 8)
        w = random.randint(1, 30)
        weights = [random.randint(0, 15) for _ in range(n)]

        input_data = f"{w} {n}\n" + " ".join(map(str, weights)) + "\n"

        expected = _brute_force(weights, w)
        got = int(check(11, input_data))

        assert got == expected, (
            f"trial #{trial}: weights={weights}, w={w}\n"
            f"expected={expected}, got={got}"
        )
