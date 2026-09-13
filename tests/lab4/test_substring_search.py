from test_utils import check


def test_minimal():
    check("substring_search", "a\na\n", "0")


def test_example_1():
    check("substring_search", "ababbababa\naba\n", "0 5 7")


def test_maximal():
    n = 50_000
    s = "a" * n
    t = "a"
    expected = " ".join(str(i) for i in range(n))
    check("substring_search", f"{s}\n{t}\n", expected, timeout=30)


def test_no_occurrences():
    check("substring_search", "abc\ndef\n", "")


def test_pattern_longer_than_text():
    check("substring_search", "ab\nabcdef\n", "")


def test_single_char_multiple():
    check("substring_search", "abacaba\na\n", "0 2 4 6")


def test_overlapping():
    check("substring_search", "aaaa\naa\n", "0 1 2")


def test_boundaries():
    check("substring_search", "abxxab\nab\n", "0 4")


def test_whole_text():
    check("substring_search", "hello\nhello\n", "0")


def test_maximal_no_occurrences():
    n = 50_000
    s = "a" * n
    t = "b" * n
    check("substring_search", f"{s}\n{t}\n", "", timeout=30)
