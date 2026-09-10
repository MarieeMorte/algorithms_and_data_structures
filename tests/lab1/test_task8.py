import random

from test_utils import check


def test_minimal():
    check(8, "1\n5 10\n", "1")


def test_example_1():
    check(8, "1\n5 10\n", "1")


def test_example_2():
    check(8, "3\n1 5\n2 3\n3 4\n", "2")


def test_maximal():
    n = 1000
    lines = [str(n)] + [f"{i + 1} {i + 2}" for i in range(n)]
    check(8, "\n".join(lines) + "\n", str(n))


def test_all_overlap():
    check(8, "3\n1 5\n2 6\n3 7\n", "1")


def test_all_disjoint():
    check(8, "4\n1 2\n3 4\n5 6\n7 8\n", "4")


def test_intervals_touch_at_endpoint():
    check(8, "2\n1 5\n5 10\n", "2")


def test_intervals_overlap_by_one():
    check(8, "2\n1 5\n4 10\n", "1")


def test_earliest_finish_wins():
    check(8, "3\n1 10\n2 3\n3 4\n", "2")


def test_not_earliest_start():
    check(8, "4\n1 10\n2 3\n3 4\n4 5\n", "3")


def test_not_shortest():
    check(8, "3\n1 2\n2 5\n3 4\n", "2")


def test_same_end_times():
    check(8, "5\n1 2\n2 3\n3 4\n0 4\n0 4\n", "3")


def test_long_lecture_first_in_input():
    check(8, "4\n1 1440\n2 3\n4 5\n6 7\n", "3")


def test_boundary_times():
    check(8, "3\n1 2\n2 1440\n1439 1440\n", "2")


def test_all_same_interval():
    check(8, "3\n5 10\n5 10\n5 10\n", "1")


def _brute_force(lectures):
    n = len(lectures)
    best = 0
    for mask in range(1 << n):
        chosen = [lectures[i] for i in range(n) if mask & (1 << i)]
        if len(chosen) <= best:
            continue
        chosen.sort()
        ok = True
        for i in range(1, len(chosen)):
            if chosen[i][0] < chosen[i - 1][1]:
                ok = False
                break
        if ok:
            best = len(chosen)
    return best


def test_stress_random_small():
    random.seed(2024)
    for trial in range(30):
        n = random.randint(1, 8)
        lectures = []
        for _ in range(n):
            start = random.randint(1, 20)
            end = random.randint(start + 1, 25)
            lectures.append((start, end))

        input_data = (
                f"{n}\n"
                + "\n".join(f"{s} {e}" for s, e in lectures)
                + "\n"
        )

        expected = _brute_force(lectures)
        got = int(check(8, input_data))

        assert got == expected, (
            f"trial #{trial}: lectures={lectures}\n"
            f"expected={expected}, got={got}"
        )
