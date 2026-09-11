from test_utils import check


def test_minimal():
    check("cyclic_string", "a\n", "1")


def test_example_1():
    check("cyclic_string", "abababa\n", "2")


def test_maximal():
    n = 50_000
    s = "a" * n
    check("cyclic_string", s + "\n", "1", timeout=30)


def test_all_different():
    check("cyclic_string", "abcdef\n", "6")


def test_two_chars():
    check("cyclic_string", "ab\n", "2")


def test_period_two():
    check("cyclic_string", "abab\n", "2")


def test_full_period():
    check("cyclic_string", "aaaaa\n", "1")


def test_no_exact_period():
    check("cyclic_string", "abcab\n", "3")


def test_period_three():
    check("cyclic_string", "abcabcab\n", "3")


def test_maximal_no_repeat():
    n = 50_000
    s = ("ab" * (n // 2 + 1))[:n]
    check("cyclic_string", s + "\n", "2", timeout=30)
