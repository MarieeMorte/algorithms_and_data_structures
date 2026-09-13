from test_utils import check


def test_minimal():
    check(10, "1\n5 0 0\n", "YES")


def test_example_1():
    check(
        10,
        "6\n"
        "-2 0 2\n"
        "8 4 3\n"
        "9 0 0\n"
        "3 6 5\n"
        "6 0 0\n"
        "0 0 0\n",
        "YES",
    )


def test_example_2():
    check(10, "0\n", "YES")


def test_example_3():
    check(
        10,
        "3\n"
        "5 2 3\n"
        "6 0 0\n"
        "4 0 0\n",
        "NO",
    )


def test_maximum():
    n = 200_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} 0 {i + 1}")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(10, input_data, "YES", timeout=60)


def test_two_nodes_valid_left():
    check(10, "2\n10 2 0\n5 0 0\n", "YES")


def test_two_nodes_valid_right():
    check(10, "2\n5 0 2\n10 0 0\n", "YES")


def test_two_nodes_invalid_left():
    check(10, "2\n5 2 0\n10 0 0\n", "NO")


def test_two_nodes_invalid_right():
    check(10, "2\n10 0 2\n5 0 0\n", "NO")


def test_left_subtree_violation():
    check(
        10,
        "3\n"
        "5 2 3\n"
        "7 0 0\n"
        "10 0 0\n",
        "NO",
    )


def test_right_subtree_violation():
    check(
        10,
        "3\n"
        "5 2 3\n"
        "3 0 0\n"
        "2 0 0\n",
        "NO",
    )


def test_deep_violation():
    check(
        10,
        "4\n"
        "10 2 3\n"
        "5 4 0\n"
        "15 0 0\n"
        "12 0 0\n",
        "NO",
    )


def test_boundary_max_int():
    check(
        10,
        "3\n"
        "0 2 3\n"
        "-1000000000 0 0\n"
        "1000000000 0 0\n",
        "YES",
    )


def test_negative_keys():
    check(
        10,
        "3\n"
        "0 2 3\n"
        "-5 0 0\n"
        "5 0 0\n",
        "YES",
    )


def test_left_chain_max():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{-i} {i + 1} 0")
    lines.append(f"{-n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(10, input_data, "YES")


def test_right_chain_max():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} 0 {i + 1}")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(10, input_data, "YES")


def test_left_chain_invalid():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"{i} {i + 1} 0")
    lines.append(f"{n} 0 0")
    input_data = "\n".join(lines) + "\n"
    check(10, input_data, "NO")


def test_full_binary_tree():
    check(
        10,
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
        "YES",
    )


def test_random_valid_bst():
    import random
    random.seed(10)
    n = 2000
    keys = sorted(random.sample(range(-10000, 10000), n))

    left = [0] * n
    right = [0] * n

    def build(lo, hi, parent_idx):
        if lo > hi:
            return 0
        mid = (lo + hi) // 2
        node = mid + 1
        l = build(lo, mid - 1, node)
        r = build(mid + 1, hi, node)
        left[mid] = l
        right[mid] = r
        return node

    build(0, n - 1, 0)
    lines = [str(n)]
    for i in range(n):
        lines.append(f"{keys[i]} {left[i]} {right[i]}")
    input_data = "\n".join(lines) + "\n"
    check(10, input_data, "YES")


def test_random_invalid_bst():
    import random
    random.seed(11)
    n = 100
    keys = [random.randint(-100, 100) for _ in range(n)]
    left = [0] * n
    right = [0] * n
    for i in range(1, n):
        parent = (i - 1) // 2
        if i % 2 == 1:
            left[parent] = i + 1
        else:
            right[parent] = i + 1
    lines = [str(n)]
    for i in range(n):
        lines.append(f"{keys[i]} {left[i]} {right[i]}")
    input_data = "\n".join(lines) + "\n"
    check(10, input_data, "NO")
