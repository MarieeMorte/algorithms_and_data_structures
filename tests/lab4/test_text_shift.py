from test_utils import check


def test_minimal():
    check("text_shift", "a\na\n", "0")


def test_example_1():
    check("text_shift", "abcde\ndeabc\n", "2")


def test_maximal():
    n = 10_000
    s = "a" * n
    t = "a" * n
    check("text_shift", f"{s}\n{t}\n", "0", timeout=30)


def test_no_shift():
    check("text_shift", "abcde\nabcde\n", "0")


def test_shift_one():
    check("text_shift", "abcde\neabcd\n", "1")


def test_shift_n_minus_one():
    check("text_shift", "abcde\nbcdea\n", "4")


def test_not_a_shift():
    check("text_shift", "abcde\nedcba\n", "-1")


def test_same_chars():
    check("text_shift", "aaaa\naaaa\n", "0")


def test_two_chars():
    check("text_shift", "ab\nba\n", "1")


def test_periodic():
    check("text_shift", "abab\nbaba\n", "1")


def test_maximal_no_shift():
    n = 10_000
    s = "a" * n
    t = "b" * n
    check("text_shift", f"{s}\n{t}\n", "-1", timeout=30)
