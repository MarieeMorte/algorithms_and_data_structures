from test_utils import check


def test_minimal():
    check(12, "1\n5 0 0\n", "0")


def test_example():
    check(
        12,
        "6\n"
        "-2 0 2\n"
        "8 4 3\n"
        "9 0 0\n"
        "3 6 5\n"
        "6 0 0\n"
        "0 0 0\n",
        "3\n-1\n0\n0\n0\n0",
    )


def test_maximum():
    n = 200_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} {i + 1} 0")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"

    expected = []
    for i in range(1, n + 1):
        left_h = n - i
        right_h = 0
        expected.append(str(right_h - left_h))

    check(12, input_data, "\n".join(expected), timeout=60)


def test_empty():
    check(12, "0\n", "")


def test_right_chain():
    n = 5
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} 0 {i + 1}")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"

    expected = []
    for i in range(1, n + 1):
        left_h = 0
        right_h = n - i
        expected.append(str(right_h - left_h))

    check(12, input_data, "\n".join(expected))


def test_two_nodes_left():
    check(12, "2\n10 2 0\n5 0 0\n", "-1\n0")


def test_two_nodes_right():
    check(12, "2\n5 0 2\n10 0 0\n", "1\n0")


def test_full_binary_tree():
    check(
        12,
        "7\n"
        "4 2 3\n"
        "2 4 5\n"
        "6 6 7\n"
        "1 0 0\n"
        "3 0 0\n"
        "5 0 0\n"
        "7 0 0\n",
        "0\n0\n0\n0\n0\n0\n0",
    )


def test_avl_balanced_tree():
    check(
        12,
        "5\n"
        "10 2 3\n"
        "5 4 5\n"
        "15 0 0\n"
        "3 0 0\n"
        "7 0 0\n",
        "-1\n0\n0\n0\n0",
    )


def test_unbalanced_root():
    check(
        12,
        "4\n"
        "1 0 2\n"
        "2 0 3\n"
        "3 0 4\n"
        "4 0 0\n",
        "3\n2\n1\n0",
    )


def test_negative_keys():
    check(
        12,
        "3\n"
        "0 2 3\n"
        "-5 0 0\n"
        "5 0 0\n",
        "0\n0\n0",
    )


def test_max_key_values():
    check(
        12,
        "3\n"
        "0 2 3\n"
        "-1000000000 0 0\n"
        "1000000000 0 0\n",
        "0\n0\n0",
    )


def test_left_chain_max():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{-i} {i + 1} 0")
    lines.append(f"{-n} 0 0")
    input_data = "\n".join(lines) + "\n"

    expected = []
    for i in range(1, n + 1):
        left_h = n - i
        expected.append(str(-left_h))

    check(12, input_data, "\n".join(expected), timeout=60)


def test_right_chain_max():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} 0 {i + 1}")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"

    expected = []
    for i in range(1, n + 1):
        right_h = n - i
        expected.append(str(right_h))

    check(12, input_data, "\n".join(expected), timeout=60)
