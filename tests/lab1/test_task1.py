import itertools
import random

from test_utils import check


def test_minimal():
    check(1, "1 0\n0 0\n", "0.0000")


def test_example_1():
    check(1, "3 50\n60 20\n100 50\n120 30\n", "180.0000")


def test_example_2():
    check(1, "1 10\n500 30\n", "166.6667")


def test_maximal():
    n = 1000
    capacity = 2 * 10 ** 6
    lines = [f"{n} {capacity}"]
    for _ in range(n):
        lines.append(f"{2 * 10 ** 6} {2 * 10 ** 6}")
    check(1, "\n".join(lines) + "\n", "2000000.0000")


def test_all_items_fit_exactly():
    check(1, "2 10\n10 5\n10 5\n", "20.0000")


def test_no_items_fit_fully():
    check(1, "2 5\n100 10\n50 10\n", "50.0000")


def test_single_item_fits_exactly():
    check(1, "1 10\n100 10\n", "100.0000")


def test_greedy_by_price_would_fail():
    check(1, "2 10\n100 50\n60 10\n", "60.0000")


def test_equal_ratios():
    check(1, "3 6\n10 3\n10 3\n10 3\n", "20.0000")


def test_take_best_ratio_first():
    check(1, "3 4\n10 1\n9 3\n8 5\n", "19.0000")


def test_zero_weight_positive_price():
    check(1, "2 5\n100 0\n50 5\n", "150.0000")


def test_zero_capacity_with_zero_weight_item():
    check(1, "1 0\n100 0\n", "100.0000")


def test_zero_capacity_nonzero_items():
    check(1, "2 0\n100 5\n50 3\n", "0.0000")


def test_rounding_precision_third():
    check(1, "1 10\n500 30\n", "166.6667")


def test_rounding_precision_seventh():
    check(1, "1 7\n100 11\n", "63.6364")


def _brute_force(items, capacity):
    n = len(items)
    best = 0.0
    for r in range(n + 1):
        for subset in itertools.combinations(range(n), r):
            used = sum(items[i][1] for i in subset)
            if used > capacity:
                continue
            value = sum(items[i][0] for i in subset)
            remaining = capacity - used
            best = max(best, value)
            for j in range(n):
                if j in subset:
                    continue
                price, weight = items[j]
                if weight == 0:
                    best = max(best, value + price)
                else:
                    take = min(remaining, weight)
                    best = max(best, value + price * take / weight)
    return best


def test_stress_random_small():
    random.seed(12345)
    for trial in range(30):
        n = random.randint(1, 5)
        capacity = random.randint(0, 20)
        items = [
            (random.randint(0, 30), random.randint(0, 10))
            for _ in range(n)
        ]
        input_data = f"{n} {capacity}\n" + "\n".join(
            f"{price} {weight}" for price, weight in items
        ) + "\n"

        expected = _brute_force(items, capacity)
        got = float(check(1, input_data))

        assert abs(got - expected) < 1e-3, (
            f"trial #{trial}: items={items}, capacity={capacity}\n"
            f"expected≈{expected}, got={got}"
        )
