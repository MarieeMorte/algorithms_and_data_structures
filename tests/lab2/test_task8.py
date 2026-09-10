from test_utils import check


def test_minimal():
    check(8, "1\n5 0 0\n", "1")


def test_example():
    check(
        8,
        "6\n"
        "-2 0 2\n"
        "8 4 3\n"
        "9 0 0\n"
        "3 6 5\n"
        "6 0 0\n"
        "0 0 0\n",
        "4",
    )


def test_maximum():
    n = 200_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} 0 {i + 1}")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(8, input_data, str(n), timeout=60)


def test_empty():
    check(8, "0\n", "0")


def test_left_chain():
    n = 1000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{-i} {i + 1} 0")
    lines.append(f"{-n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(8, input_data, str(n))


def test_full_binary_tree():
    # Полное дерево высоты 4: 15 вершин
    check(
        8,
        "15\n"
        "8 2 3\n"
        "4 4 5\n"
        "12 6 7\n"
        "2 8 9\n"
        "6 10 11\n"
        "10 12 13\n"
        "14 14 15\n"
        "1 0 0\n"
        "3 0 0\n"
        "5 0 0\n"
        "7 0 0\n"
        "9 0 0\n"
        "11 0 0\n"
        "13 0 0\n"
        "15 0 0\n",
        "4",
    )


def test_two_nodes_left():
    check(8, "2\n10 2 0\n5 0 0\n", "2")


def test_two_nodes_right():
    check(8, "2\n5 0 2\n10 0 0\n", "2")


def test_unbalanced_left_deep():
    # Левая ветка глубокая, правая короткая
    check(
        8,
        "5\n"
        "10 2 3\n"
        "5 4 5\n"
        "15 0 0\n"
        "3 0 0\n"
        "7 0 0\n",
        "3",
    )


def test_zigzag():
    # Зигзаг: корень -> левый -> правый -> левый
    check(
        8,
        "4\n"
        "10 2 0\n"
        "5 0 3\n"
        "7 4 0\n"
        "6 0 0\n",
        "4",
    )


def test_max_depth_right():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} 0 {i + 1}")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(8, input_data, str(n))


def test_max_depth_left():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{-i} {i + 1} 0")
    lines.append(f"{-n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(8, input_data, str(n))


def test_max_key_values():
    check(
        8,
        "3\n"
        "0 2 3\n"
        "-1000000000 0 0\n"
        "1000000000 0 0\n",
        "2",
    )
