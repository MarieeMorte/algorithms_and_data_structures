from test_utils import check


def test_minimal():
    check(2, "a\n", "0")


def test_example_1():
    check(2, "treasure\n", "8")


def test_example_2():
    check(2, "you will never find the treasure\n", "146")


def test_maximal():
    n = 300_000
    s = "a" * n
    expected = str(n * (n - 1) * (n - 2) // 6)
    check(2, s + "\n", expected)


def test_two_chars():
    check(2, "ab\n", "0")


def test_three_same():
    check(2, "aaa\n", "1")


def test_three_different():
    check(2, "abc\n", "0")


def test_palindrome_itself():
    check(2, "aba\n", "1")


def test_with_spaces():
    check(2, "a b a\n", "1")


def test_all_spaces_between():
    check(2, "a   b   a\n", "1")


def test_two_letters_aba_pattern():
    check(2, "abab\n", "2")


def test_repeated_single_char():
    check(2, "aaaa\n", "4")


def test_mixed_case_1():
    check(2, "abcba\n", "4")


def test_mixed_case_2():
    check(2, "aabaa\n", "8")


def test_maximal_with_spaces():
    n = 100_000
    s = ("a" * n + " ") * 2 + "a" * n
    expected = str((3 * n) * (3 * n - 1) * (3 * n - 2) // 6)
    check(2, s + "\n", expected)
