import random

from test_utils import check


def _brute_force(m, n):
    cells = m * n
    count = 0
    for bits in range(1 << cells):
        grid = [[(bits >> (r * n + c)) & 1 for c in range(n)] for r in range(m)]
        ok = True
        for r in range(m - 1):
            for c in range(n - 1):
                if grid[r][c] == grid[r][c + 1] == grid[r + 1][c] == grid[r + 1][c + 1]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count


def test_minimal():
    check(22, "1 1\n", "2")


def test_example_1():
    check(22, "2 2\n", "14")


def test_example_2():
    check(22, "3 3\n", "322")


def test_maximal():
    check(22, "1 30\n", str(2 ** 30), timeout=30)


def test_1xN():
    check(22, "1 2\n", "4")
    check(22, "1 3\n", "8")
    check(22, "1 4\n", "16")
    check(22, "1 5\n", "32")


def test_Nx1():
    check(22, "2 1\n", "4")
    check(22, "3 1\n", "8")
    check(22, "4 1\n", "16")


def test_symmetry():
    for m, n in [(2, 3), (2, 4), (3, 4)]:
        out1 = check(22, f"{m} {n}\n")
        out2 = check(22, f"{n} {m}\n")
        assert out1 == out2, f"asymmetric for {m}x{n}: {out1} vs {out2}"


def test_2x3():
    check(22, "2 3\n", str(_brute_force(2, 3)))


def test_3x2():
    check(22, "3 2\n", str(_brute_force(3, 2)))


def test_2x4():
    check(22, "2 4\n", str(_brute_force(2, 4)))


def test_stress_random_small():
    random.seed(22)
    for trial in range(10):
        m = random.randint(1, 4)
        n = random.randint(1, 4)
        if m * n > 16:
            continue
        expected = str(_brute_force(m, n))
        got = check(22, f"{m} {n}\n")
        assert got == expected, (
            f"trial #{trial}: {m}x{n}, expected={expected}, got={got}"
        )
