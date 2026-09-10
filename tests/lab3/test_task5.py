from test_utils import check


def test_minimal():
    check(5, "1 0\n", "1")


def test_example_1():
    check(5, "4 4\n1 2\n4 1\n2 3\n3 1\n", "2")


def test_example_2():
    check(5, "5 7\n2 1\n3 2\n3 1\n4 3\n4 1\n5 2\n5 3\n", "5")


def test_maximal_isolated():
    n = 10000
    m = 0
    lines = [f"{n} {m}"]
    check(5, "\n".join(lines) + "\n", str(n))


def test_maximal_cycle():
    n = 10000
    m = n
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    lines.append(f"{n} 1")
    check(5, "\n".join(lines) + "\n", "1")


def test_two_scc():
    check(5, "4 4\n1 2\n2 1\n3 4\n4 3\n", "2")


def test_chain():
    check(5, "4 3\n1 2\n2 3\n3 4\n", "4")


def test_star():
    check(5, "5 4\n1 2\n1 3\n1 4\n1 5\n", "5")


def test_cycle_and_isolated():
    check(5, "4 3\n1 2\n2 3\n3 1\n", "2")
