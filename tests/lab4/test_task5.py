from test_utils import check


def test_minimal():
    check(5, "a\n", "0")


def test_example_1():
    check(5, "aaaAAA\n", "0 1 2 0 0 0")


def test_example_2():
    check(5, "abacaba\n", "0 0 1 0 1 2 3")


def test_maximal():
    n = 10 ** 6
    s = "a" * n
    expected = " ".join(str(i) for i in range(n))
    check(5, s + "\n", expected, timeout=30)


def test_all_different():
    check(5, "abcdef\n", "0 0 0 0 0 0")


def test_all_same():
    check(5, "aaaaa\n", "0 1 2 3 4")


def test_two_chars():
    check(5, "ab\n", "0 0")


def test_periodic():
    check(5, "ababab\n", "0 0 1 2 3 4")


def test_maximal_no_match():
    n = 10 ** 6
    s = ("ab" * (n // 2 + 1))[:n]
    expected = [0, 0] + [i - 1 for i in range(2, n)]
    check(5, s + "\n", " ".join(map(str, expected)), timeout=30)
