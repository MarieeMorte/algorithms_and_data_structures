from test_utils import check


def test_minimal():
    check(10, "1 0\n1\n", "0")


def test_example_1():
    check(10, "6 7\n1 2 10\n2 3 5\n1 3 100\n3 5 7\n5 4 10\n4 3 -18\n6 1 -1\n1\n",
          "0\n10\n-\n-\n-\n*")


def test_example_2():
    check(10, "5 4\n1 2 1\n4 1 2\n2 3 2\n3 1 -5\n4\n",
          "-\n-\n-\n0\n*")


def test_maximal():
    n = 1000
    m = 999
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1} 1")
    lines.append("1")
    expected = "\n".join(str(i) for i in range(n))
    check(10, "\n".join(lines) + "\n", expected)


def test_no_edges():
    check(10, "3 0\n1\n", "0\n*\n*")


def test_no_path():
    check(10, "3 1\n2 3 5\n1\n", "0\n*\n*")


def test_negative_cycle_from_start():
    check(10, "3 3\n1 2 1\n2 3 1\n3 1 -5\n1\n", "-\n-\n-")


def test_negative_cycle_unreachable():
    check(10, "6 6\n1 2 1\n4 5 -1\n5 6 -1\n6 4 -1\n2 3 1\n1 3 5\n1\n",
          "0\n1\n2\n*\n*\n*")


def test_negative_reachable_through_positive():
    check(10, "5 5\n1 2 5\n2 3 5\n3 4 1\n4 3 -3\n3 5 1\n1\n",
          "0\n5\n-\n-\n-")


def test_negative_edges_no_cycle():
    check(10, "4 4\n1 2 -1\n2 3 -1\n3 4 -1\n4 4 5\n1\n", "0\n-1\n-2\n-3")


def test_direct_longer():
    check(10, "3 3\n1 2 1\n2 3 1\n1 3 5\n1\n", "0\n1\n2")


def test_start_not_first():
    check(10, "4 3\n1 2 1\n2 3 1\n2 4 1\n2\n", "*\n0\n1\n1")


def test_all_unreachable_except_start():
    check(10, "5 2\n2 3 1\n3 4 1\n1\n", "0\n*\n*\n*\n*")
