from test_utils import check


def test_minimal():
    check(2, "1 0\n", "1")


def test_example_1():
    check(2, "4 2\n1 2\n3 2\n", "2")


def test_maximal():
    n = 1000
    m = 999
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    check(2, "\n".join(lines) + "\n", "1")


def test_all_isolated():
    n = 1000
    lines = [f"{n} 0"]
    check(2, "\n".join(lines) + "\n", "1000")


def test_two_components():
    check(2, "6 4\n1 2\n2 3\n4 5\n5 6\n", "2")


def test_three_components():
    check(2, "7 4\n1 2\n3 4\n5 6\n6 7\n", "3")


def test_isolated_vertices():
    check(2, "5 1\n1 2\n", "4")


def test_chain():
    check(2, "5 4\n1 2\n2 3\n3 4\n4 5\n", "1")


def test_star():
    check(2, "5 4\n1 2\n1 3\n1 4\n1 5\n", "1")


def test_cycle():
    check(2, "4 4\n1 2\n2 3\n3 4\n4 1\n", "1")
