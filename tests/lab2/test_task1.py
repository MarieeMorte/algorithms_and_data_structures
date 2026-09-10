import random

from test_utils import check


def test_minimal():
    check(1, "1\n42 -1 -1\n", "42\n42\n42")


def test_example_1():
    check(
        1,
        "5\n"
        "4 1 2\n"
        "2 3 4\n"
        "5 -1 -1\n"
        "1 -1 -1\n"
        "3 -1 -1\n",
        "1 2 3 4 5\n"
        "4 2 1 3 5\n"
        "1 3 2 5 4",
    )


def test_example_2():
    check(
        1,
        "10\n"
        "0 7 2\n"
        "10 -1 -1\n"
        "20 -1 6\n"
        "30 8 9\n"
        "40 3 -1\n"
        "50 -1 -1\n"
        "60 1 -1\n"
        "70 5 4\n"
        "80 -1 -1\n"
        "90 -1 -1\n",
        "50 70 80 30 90 40 0 20 10 60\n"
        "0 70 50 40 30 80 90 20 60 10\n"
        "50 80 90 30 40 70 10 60 20 0",
    )


def test_maximum():
    n = 100_000
    lines = [str(n)]
    for i in range(n - 1):
        lines.append(f"{i} -1 {i + 1}")
    lines.append(f"{n - 1} -1 -1")
    input_data = "\n".join(lines) + "\n"

    expected_in = " ".join(str(i) for i in range(n))
    expected_pre = " ".join(str(i) for i in range(n))
    expected_post = " ".join(str(i) for i in range(n - 1, -1, -1))

    check(1, input_data, f"{expected_in}\n{expected_pre}\n{expected_post}")


def test_two_nodes_left():
    check(1, "2\n10 1 -1\n5 -1 -1\n", "5 10\n10 5\n5 10")


def test_two_nodes_right():
    check(1, "2\n10 -1 1\n5 -1 -1\n", "10 5\n10 5\n5 10")


def test_chain_left_max():
    n = 100_000
    lines = [str(n)]
    for i in range(n - 1):
        lines.append(f"{i} {i + 1} -1")
    lines.append(f"{n - 1} -1 -1")
    input_data = "\n".join(lines) + "\n"

    expected_in = " ".join(str(i) for i in range(n - 1, -1, -1))
    expected_pre = " ".join(str(i) for i in range(n))
    expected_post = " ".join(str(i) for i in range(n - 1, -1, -1))

    check(1, input_data, f"{expected_in}\n{expected_pre}\n{expected_post}")


def test_max_values_keys():
    check(
        1,
        "3\n"
        "1000000000 1 2\n"
        "0 -1 -1\n"
        "999999999 -1 -1\n",
        "0 1000000000 999999999\n"
        "1000000000 0 999999999\n"
        "0 999999999 1000000000",
    )


def test_full_binary_tree():
    check(
        1,
        "7\n"
        "4 1 2\n"
        "2 3 4\n"
        "6 5 6\n"
        "1 -1 -1\n"
        "3 -1 -1\n"
        "5 -1 -1\n"
        "7 -1 -1\n",
        "1 2 3 4 5 6 7\n"
        "4 2 1 3 6 5 7\n"
        "1 3 2 5 7 6 4",
    )


def test_stress_random_structure():
    random.seed(12345)
    n = 5000

    keys = list(range(n))
    random.shuffle(keys)

    left = [-1] * n
    right = [-1] * n
    for i in range(n):
        if i > 0:
            while True:
                parent = random.randint(0, i - 1)
                side = random.randint(0, 1)
                if side == 0 and left[parent] == -1:
                    left[parent] = i
                    break
                if side == 1 and right[parent] == -1:
                    right[parent] = i
                    break

    lines = [str(n)]
    for i in range(n):
        lines.append(f"{keys[i]} {left[i]} {right[i]}")
    input_data = "\n".join(lines) + "\n"

    def inorder(v):
        if v == -1:
            return []
        return inorder(left[v]) + [keys[v]] + inorder(right[v])

    def preorder(v):
        if v == -1:
            return []
        return [keys[v]] + preorder(left[v]) + preorder(right[v])

    def postorder(v):
        if v == -1:
            return []
        return postorder(left[v]) + postorder(right[v]) + [keys[v]]

    expected = (
            " ".join(map(str, inorder(0))) + "\n"
            + " ".join(map(str, preorder(0))) + "\n"
            + " ".join(map(str, postorder(0)))
    )

    check(1, input_data, expected)
