from test_utils import check


def test_minimal():
    check(8, "2 1\n1 2 5\n1 2\n", "5")


def test_example_1():
    check(8, "4 4\n1 2 1\n4 1 2\n2 3 2\n1 3 5\n1 3\n", "3")


def test_example_2():
    check(8, "5 9\n1 2 4\n1 3 2\n2 3 2\n3 2 1\n2 4 2\n3 5 4\n5 4 1\n2 5 3\n3 4 4\n1 5\n", "6")


def test_example_3():
    check(8, "3 3\n1 2 7\n1 3 5\n2 3 2\n3 2\n", "-1")


def test_maximal():
    n = 10000
    m = 9999
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1} 1")
    lines.append(f"1 {n}")
    check(8, "\n".join(lines) + "\n", str(n - 1))


def test_no_edges():
    check(8, "2 0\n1 2\n", "-1")


def test_no_path():
    check(8, "4 2\n1 2 5\n3 4 3\n1 4\n", "-1")


def test_direct_shorter():
    check(8, "3 3\n1 2 1\n2 3 1\n1 3 5\n1 3\n", "2")


def test_direct_longer():
    check(8, "3 3\n1 2 1\n2 3 1\n1 3 5\n1 2\n", "1")


def test_start_equals_target():
    check(8, "2 1\n1 2 5\n1 1\n", "0")


def test_zero_weight_edges():
    check(8, "4 4\n1 2 0\n2 3 0\n3 4 0\n1 4 5\n1 4\n", "0")


def test_multiple_paths():
    check(8, "5 6\n1 2 1\n1 3 4\n2 4 2\n3 4 1\n4 5 3\n1 5 10\n1 5\n", "6")


def test_large_weights():
    check(8, "3 3\n1 2 100000000\n2 3 100000000\n1 3 999999999\n1 3\n", "200000000")


def test_reverse_direction():
    check(8, "3 2\n1 2 5\n2 3 5\n3 1\n", "-1")
