from test_utils import check


def test_minimal():
    check(1, "2 1\n1 2\n1 2\n", "1")


def test_example_1():
    check(1, "4 4\n1 2\n3 2\n4 3\n1 4\n1 4\n", "1")


def test_example_2():
    check(1, "4 2\n1 2\n3 2\n1 4\n", "0")


def test_maximal():
    n = 1000
    lines = [f"{n} {n}"]  # m = n = 1000
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    lines.append(f"1 {n}")  # 1000-е ребро
    lines.append("1 1000")
    input_data = "\n".join(lines) + "\n"
    check(1, input_data, "1")


def test_no_path():
    check(1, "4 2\n1 2\n3 4\n1 3\n", "0")


def test_path_through_multiple_vertices():
    check(1, "5 4\n1 2\n2 3\n3 4\n4 5\n1 5\n", "1")


def test_isolated_vertex():
    check(1, "3 1\n1 2\n1 3\n", "0")


def test_self_loop_not_allowed_by_constraints():
    pass


def test_reverse_order():
    check(1, "4 4\n1 2\n3 2\n4 3\n1 4\n4 1\n", "1")


def test_large_disconnected():
    n = 1000
    m = 500
    lines = [f"{n} {m}"]
    for i in range(1, n, 2):
        lines.append(f"{i} {i + 1}")
    lines.append("1 3")
    input_data = "\n".join(lines) + "\n"
    check(1, input_data, "0")


def test_long_path():
    n = 100
    lines = [f"{n} {n - 1}"]
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
    lines.append("1 100")
    input_data = "\n".join(lines) + "\n"
    check(1, input_data, "1")
