from test_utils import check


def test_minimal():
    check(7, "a a\n", "0 0 1")


def test_example_1():
    check(
        7,
        "cool toolbox\naaa bb\naabaa babbaab\n",
        "1 1 3\n0 0 0\n2 3 3",
    )


def test_maximal():
    n = 100_000
    s = "a" * (n // 2)
    t = "a" * (n // 2)
    check(7, f"{s} {t}\n", f"0 0 {n // 2}", timeout=30)


def test_no_common():
    check(7, "abc def\n", "0 0 0")


def test_single_char_common():
    check(7, "a a\n", "0 0 1")


def test_whole_string_common():
    check(7, "abc abc\n", "0 0 3")


def test_suffix_prefix():
    check(7, "abcde cdeab\n", "2 0 3")


def test_repeated_chars():
    check(7, "aaaa aaaa\n", "0 0 4")


def test_common_at_end():
    check(7, "xyzab ab\n", "3 0 2")


def test_different_lengths():
    check(7, "a ab\n", "0 0 1")


def test_maximal_no_common():
    n = 100_000
    s = "a" * (n // 2)
    t = "b" * (n // 2)
    check(7, f"{s} {t}\n", "0 0 0", timeout=30)


def test_maximal_multiple_pairs():
    pairs = []
    for _ in range(10):
        s = "a" * 5_000
        t = "a" * 5_000
        pairs.append(f"{s} {t}")
    expected = "\n".join(["0 0 5000"] * 10)
    check(7, "\n".join(pairs) + "\n", expected, timeout=30)
