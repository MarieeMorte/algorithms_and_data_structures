from test_utils import check


def test_minimal():
    check(3, "a\na\n", "1\n1")


def test_example_1():
    check(3, "aba\nabacaba\n", "2\n1 5")


def test_example_2():
    check(3, "Test\ntestTesttesT\n", "1\n5")


def test_example_3():
    check(3, "aaaaa\nbaaaaaaa\n", "3\n2 3 4")


def test_maximal():
    n = 10 ** 6
    p = "a"
    t = "a" * n
    positions = " ".join(str(i) for i in range(1, n + 1))
    check(3, f"{p}\n{t}\n", f"{n}\n{positions}", timeout=30)


def test_no_occurrences():
    check(3, "abc\ndefdef\n", "0")


def test_pattern_longer_than_text():
    check(3, "abcdef\nabc\n", "0")


def test_overlapping():
    check(3, "aa\naaaa\n", "3\n1 2 3")


def test_boundaries():
    check(3, "ab\nabxxab\n", "2\n1 5")


def test_case_sensitive():
    check(3, "abc\nABCabcABC\n", "1\n4")


def test_maximal_no_occurrences():
    n = 10 ** 6
    p = "a" * n
    t = "b" * n
    check(3, f"{p}\n{t}\n", "0", timeout=30)


def test_maximal_half_occurrences():
    n = 10 ** 6
    p = "ab"
    t = "ab" * (n // 2)
    positions = " ".join(str(i) for i in range(1, n, 2))
    check(3, f"{p}\n{t}\n", f"{n // 2}\n{positions}", timeout=30)
