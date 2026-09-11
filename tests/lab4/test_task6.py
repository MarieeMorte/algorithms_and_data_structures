from test_utils import check


def test_minimal():
    check(6, "aa\n", "1")


def test_example_1():
    check(6, "aaaAAA\n", "2 1 0 0 0")


def test_example_2():
    check(6, "abacaba\n", "0 1 0 3 0 1")


def test_maximal():
    n = 10 ** 6
    s = "a" * n
    expected = " ".join(str(n - i - 1) for i in range(n - 1))
    check(6, s + "\n", expected, timeout=30)


def test_all_different():
    check(6, "abcdef\n", "0 0 0 0 0")


def test_all_same():
    check(6, "aaaaa\n", "4 3 2 1")


def test_two_chars_different():
    check(6, "ab\n", "0")


def test_two_chars_same():
    check(6, "aa\n", "1")


def test_periodic():
    check(6, "ababab\n", "0 4 0 2 0")


def test_maximal_no_match():
    n = 10 ** 6
    s = ("ab" * (n // 2 + 1))[:n]
    expected = []
    for i in range(1, n):
        if i % 2 == 0:
            expected.append(n - i)
        else:
            expected.append(0)
    check(6, s + "\n", " ".join(map(str, expected)), timeout=30)
