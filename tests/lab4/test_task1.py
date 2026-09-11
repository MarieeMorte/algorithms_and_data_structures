from test_utils import check


def test_minimal():
    check(1, "a\na\n", "1\n1")


def test_example_1():
    check(1, "aba\nabaCaba\n", "2\n1 5")


def test_maximal():
    n = 10_000
    p = "a" * n
    t = "a" * n
    check(1, f"{p}\n{t}\n", f"1\n1")


def test_no_occurrences():
    check(1, "abc\ndefdef\n", "0")


def test_pattern_longer_than_text():
    check(1, "abcdef\nabc\n", "0")


def test_single_char_multiple_occurrences():
    check(1, "a\nabacaba\n", "4\n1 3 5 7")


def test_overlapping_occurrences():
    check(1, "aa\naaaa\n", "3\n1 2 3")


def test_occurrences_at_boundaries():
    check(1, "ab\nabxxab\n", "2\n1 5")


def test_whole_text_is_pattern():
    check(1, "hello\nhello\n", "1\n1")


def test_all_same_characters():
    check(1, "aaa\naaaaa\n", "3\n1 2 3")


def test_maximal_no_occurrences():
    n = 10_000
    p = "a" * n
    t = "b" * n
    check(1, f"{p}\n{t}\n", "0")


def test_maximal_overlapping():
    n = 10_000
    p = "aa"
    t = "a" * n
    expected_positions = " ".join(str(i) for i in range(1, n))
    check(1, f"{p}\n{t}\n", f"{n - 1}\n{expected_positions}")
