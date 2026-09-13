from test_utils import check


def test_minimal():
    check(3, "1 0\n", "0")


def test_example_1():
    check(3, "4 4\n1 2\n4 1\n2 3\n3 1\n", "1")


def test_example_2():
    check(3, "5 7\n1 2\n2 3\n1 3\n3 4\n1 4\n2 5\n3 5\n", "0")


def test_maximal():
    n = 1000
    m = 999
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    check(3, "\n".join(lines) + "\n", "0")


def test_maximal_with_cycle():
    n = 1000
    m = 1000
    lines = [f"{n} {m}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    lines.append(f"{n} 1")
    check(3, "\n".join(lines) + "\n", "1")


def test_self_loop():
    check(3, "2 1\n1 1\n", "1")


def test_two_cycle():
    check(3, "2 2\n1 2\n2 1\n", "1")


def test_no_edges():
    check(3, "5 0\n", "0")


def test_isolated_cycle():
    check(3, "6 4\n1 2\n2 3\n3 1\n4 5\n", "1")


def test_dag_with_multiple_paths():
    check(3, "4 4\n1 2\n1 3\n2 4\n3 4\n", "0")


def test_long_chain_no_cycle():
    n = 500
    lines = [f"{n} {n - 1}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    check(3, "\n".join(lines) + "\n", "0")
