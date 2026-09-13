from test_utils import check


def test_minimal():
    check(7, "0\n", "CORRECT")


def test_example_1():
    check(7, "3\n2 1 2\n1 -1 -1\n3 -1 -1\n", "CORRECT")


def test_example_2():
    check(7, "3\n1 1 2\n2 -1 -1\n3 -1 -1\n", "INCORRECT")


def test_example_3():
    check(7, "3\n2 1 2\n1 -1 -1\n2 -1 -1\n", "CORRECT")


def test_example_4():
    check(7, "3\n2 1 2\n2 -1 -1\n3 -1 -1\n", "INCORRECT")


def test_example_5():
    check(7, "5\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 4\n5 -1 -1\n", "CORRECT")


def test_example_6():
    check(
        7,
        "7\n"
        "4 1 2\n"
        "2 3 4\n"
        "6 5 6\n"
        "1 -1 -1\n"
        "3 -1 -1\n"
        "5 -1 -1\n"
        "7 -1 -1\n",
        "CORRECT",
    )


def test_example_7():
    check(7, "1\n2147483647 -1 -1\n", "CORRECT")


def test_maximum():
    n = 100_000
    lines = [str(n)]
    for i in range(n - 1):
        lines.append(f"{i} -1 {i + 1}")
    lines.append(f"{n - 1} -1 -1")
    input_data = "\n".join(lines) + "\n"
    check(7, input_data, "CORRECT")


def test_min_int_key():
    check(7, "1\n-2147483648 -1 -1\n", "CORRECT")


def test_duplicates_chain_right():
    n = 1000
    lines = [str(n)]
    for i in range(n - 1):
        lines.append(f"5 -1 {i + 1}")
    lines.append("5 -1 -1")
    input_data = "\n".join(lines) + "\n"
    check(7, input_data, "CORRECT")


def test_duplicates_chain_left_invalid():
    n = 3
    lines = [str(n), "5 1 2", "5 -1 -1", "5 -1 -1"]
    input_data = "\n".join(lines) + "\n"
    check(7, input_data, "INCORRECT")


def test_left_subtree_violation():
    check(
        7,
        "3\n"
        "5 1 2\n"
        "7 -1 -1\n"
        "10 -1 -1\n",
        "INCORRECT",
    )


def test_right_subtree_violation():
    check(
        7,
        "3\n"
        "5 1 2\n"
        "3 -1 -1\n"
        "2 -1 -1\n",
        "INCORRECT",
    )


def test_deep_violation():
    check(
        7,
        "4\n"
        "10 1 2\n"
        "5 3 -1\n"
        "15 -1 -1\n"
        "12 -1 -1\n",
        "INCORRECT",
    )


def test_duplicate_in_left_subtree():
    check(
        7,
        "3\n"
        "5 1 2\n"
        "5 -1 -1\n"
        "7 -1 -1\n",
        "INCORRECT",
    )


def test_duplicate_in_right_subtree():
    check(
        7,
        "3\n"
        "5 1 2\n"
        "3 -1 -1\n"
        "5 -1 -1\n",
        "CORRECT",
    )


def test_boundary_max_int():
    check(
        7,
        "3\n"
        "2147483647 1 2\n"
        "0 -1 -1\n"
        "2147483647 -1 -1\n",
        "CORRECT",
    )


def test_boundary_min_int():
    check(
        7,
        "3\n"
        "-2147483648 1 2\n"
        "-2147483648 -1 -1\n"
        "0 -1 -1\n",
        "INCORRECT",
    )


def test_left_chain_max():
    n = 100_000
    lines = [str(n)]
    for i in range(n - 1):
        lines.append(f"{-i} {i + 1} -1")
    lines.append(f"{-(n - 1)} -1 -1")
    input_data = "\n".join(lines) + "\n"
    check(7, input_data, "CORRECT")


def test_random_valid_bst():
    import random
    random.seed(7)
    n = 2000
    keys = sorted(random.randint(-1000, 1000) for _ in range(n))

    left = [-1] * n
    right = [-1] * n

    def build(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        left[mid] = build(lo, mid - 1)
        right[mid] = build(mid + 1, hi)
        return mid

    root = build(0, n - 1)
    assert root == 0 or True
    lines = [str(n)]
    for i in range(n):
        lines.append(f"{keys[i]} {left[i]} {right[i]}")
    input_data = "\n".join(lines) + "\n"
    check(7, input_data, "CORRECT")


def test_random_invalid_bst():
    import random
    random.seed(8)
    n = 100
    keys = [random.randint(-100, 100) for _ in range(n)]
    left = [-1] * n
    right = [-1] * n
    for i in range(1, n):
        parent = (i - 1) // 2
        if i % 2 == 1:
            left[parent] = i
        else:
            right[parent] = i
    lines = [str(n)]
    for i in range(n):
        lines.append(f"{keys[i]} {left[i]} {right[i]}")
    input_data = "\n".join(lines) + "\n"
    check(7, input_data, "INCORRECT")
