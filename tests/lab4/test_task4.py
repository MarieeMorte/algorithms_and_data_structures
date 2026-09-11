from test_utils import check


def test_minimal():
    check(4, "a\n1\n0 0 1\n", "Yes")


def test_example_1():
    check(4, "trololo\n4\n0 0 7\n2 4 3\n3 5 1\n1 3 2\n", "Yes\nYes\nYes\nNo")


def test_maximal():
    n = 500_000
    s = "a" * n
    q = 100_000
    lines = [s, str(q)]
    for _ in range(q):
        lines.append("0 0 1")
    expected = "\n".join(["Yes"] * q)
    check(4, "\n".join(lines) + "\n", expected, timeout=60)


def test_single_char():
    check(4, "a\n2\n0 0 1\n0 0 1\n", "Yes\nYes")


def test_not_equal():
    check(4, "ab\n1\n0 1 1\n", "No")


def test_two_equal():
    check(4, "abab\n2\n0 2 2\n1 1 2\n", "Yes\nYes")


def test_overlapping():
    check(4, "aaaa\n3\n0 1 3\n1 2 2\n0 3 1\n", "Yes\nYes\nYes")


def test_same_substring_different_position():
    check(4, "abcabc\n1\n0 3 3\n", "Yes")


def test_length_one():
    check(4, "abcdef\n3\n0 0 1\n0 5 1\n2 2 1\n", "Yes\nNo\nYes")


def test_different_lengths():
    check(4, "abcdef\n3\n0 3 3\n1 4 2\n0 1 4\n", "No\nNo\nNo")


def test_maximal_no_match():
    n = 500_000
    s = "a" * (n // 2) + "b" * (n // 2)
    q = 100_000
    lines = [s, str(q)]
    for _ in range(q):
        lines.append(f"0 {n // 2} 1")
    expected = "\n".join(["No"] * q)
    check(4, "\n".join(lines) + "\n", expected, timeout=60)
