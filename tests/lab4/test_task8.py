from test_utils import check


def test_minimal():
    check(8, "0 a a\n", "1 0")


def test_example_1():
    check(
        8,
        "0 ababab baaa\n1 ababab baaa\n1 xabcabc ccc\n2 xabcabc ccc\n3 aaa xxx\n",
        "0\n1 1\n0\n4 1 2 3 4\n1 0",
    )


def test_maximal():
    n = 200_000
    t = "a" * n
    p = "a" * 100_000
    positions = " ".join(str(i) for i in range(n - len(p) + 1))
    expected = f"{n - len(p) + 1} {positions}"
    check(8, f"0 {t} {p}\n", expected, timeout=60)


def test_no_matches():
    check(8, "0 abc def\n", "0")


def test_exact_match():
    check(8, "0 abc abc\n", "1 0")


def test_one_mismatch():
    check(8, "1 abc abd\n", "1 0")


def test_all_mismatches():
    check(8, "2 abc xyz\n", "0")


def test_k_zero():
    check(8, "0 aaaa aaa\n", "2 0 1")


def test_k_ge_mismatches():
    check(8, "5 abc xyz\n", "1 0")


def test_overlapping():
    check(8, "1 aaaa aaaa\n", "1 0")


def test_maximal_k5():
    t = "a" * 100_000
    p = "b" * 100_000
    check(8, f"5 {t} {p}\n", "0", timeout=60)
