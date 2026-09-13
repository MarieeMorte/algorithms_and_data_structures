from test_utils import check


def test_minimal():
    check(9, "a\n", "a")


def test_example_1():
    check(9, "ABCABCDEDEDEF\n", "ABC*2+DE*3+F")


def test_example_2():
    check(9, "Hello\n", "Hello")


def test_maximal():
    n = 5000
    s = "a" * n
    check(9, s + "\n", f"a*{n}", timeout=30)


def test_single_repeat():
    check(9, "aa\n", "aa")


def test_no_repeat():
    check(9, "abc\n", "abc")


def test_two_blocks():
    check(9, "abab\n", "abab")


def test_multiple_blocks():
    check(9, "aabaab\n", "aab*2")


def test_full_repeat_with_tail():
    check(9, "abcabcx\n", "abc*2+x")


def test_all_same_plus_other():
    check(9, "aaaaab\n", "a*5+b")


def test_block_then_repeat():
    check(9, "xabcabc\n", "x+abc*2")


def test_maximal_no_repeat():
    n = 5000
    s = "ab" * (n // 2)
    check(9, s + "\n", f"ab*{n // 2}", timeout=30)
