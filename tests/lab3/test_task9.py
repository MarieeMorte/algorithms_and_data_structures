from test_utils import check


def test_minimal():
    check(9, "1 0\n", "0")


def test_example_1():
    check(9, "4 4\n1 2 -5\n4 1 2\n2 3 2\n3 1 1\n", "1")


def test_maximal():
    n = 1000
    m = 1000
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1} 1")
    lines.append(f"{n} 1 1")
    check(9, "\n".join(lines) + "\n", "0")


def test_maximal_with_negative_cycle():
    n = 1000
    m = 1000
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1} 1")
    lines.append(f"{n} 1 -1000")
    check(9, "\n".join(lines) + "\n", "1")


def test_no_edges():
    check(9, "5 0\n", "0")


def test_self_loop_negative():
    check(9, "2 1\n1 1 -1\n", "1")


def test_self_loop_positive():
    check(9, "2 1\n1 1 5\n", "0")


def test_two_cycle_negative():
    check(9, "2 2\n1 2 -1\n2 1 -1\n", "1")


def test_two_cycle_positive():
    check(9, "2 2\n1 2 1\n2 1 1\n", "0")


def test_dag_no_cycle():
    check(9, "4 4\n1 2 -5\n1 3 -3\n2 4 -1\n3 4 -2\n", "0")


def test_negative_cycle_unreachable():
    check(9, "6 6\n1 2 1\n2 3 1\n3 1 1\n4 5 -1\n5 6 -1\n6 4 -1\n", "1")


def test_zero_weights():
    check(9, "3 3\n1 2 0\n2 3 0\n3 1 0\n", "0")


def test_large_negative():
    check(9, "3 3\n1 2 -10000\n2 3 -10000\n3 1 -10000\n", "1")
