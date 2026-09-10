from test_utils import check


def test_minimal():
    check(11, "exists 0\n", "false")


def test_example():
    check(
        11,
        "insert 2\n"
        "insert 5\n"
        "insert 3\n"
        "exists 2\n"
        "exists 4\n"
        "next 4\n"
        "prev 4\n"
        "delete 5\n"
        "next 4\n"
        "prev 4\n",
        "true\nfalse\n5\n3\nnone\n3",
    )


def test_maximum():
    n = 100_000
    lines = []
    for i in range(n):
        lines.append(f"insert {i}")
    for i in range(n):
        lines.append(f"exists {i}")
    for i in range(0, n - 1):
        lines.append(f"next {i}")
    for i in range(1, n):
        lines.append(f"prev {i}")
    input_data = "\n".join(lines) + "\n"

    expected = []
    for i in range(n):
        expected.append("true")
    for i in range(0, n - 1):
        expected.append(str(i + 1))
    for i in range(1, n):
        expected.append(str(i - 1))

    check(11, input_data, "\n".join(expected), timeout=60)


def test_empty_tree():
    check(11, "next 0\nprev 0\n", "none\nnone")


def test_insert_duplicates():
    check(
        11,
        "insert 5\ninsert 5\ninsert 5\nexists 5\n",
        "true",
    )


def test_delete_nonexistent():
    check(
        11,
        "insert 1\ndelete 2\nexists 1\nexists 2\n",
        "true\nfalse",
    )


def test_delete_leaf():
    check(
        11,
        "insert 1\ninsert 2\ninsert 3\ndelete 3\nexists 3\nnext 2\n",
        "false\nnone",
    )


def test_delete_node_with_one_child():
    check(
        11,
        "insert 1\ninsert 2\ninsert 3\ndelete 2\nexists 2\nnext 1\nprev 3\n",
        "false\n3\n1",
    )


def test_delete_node_with_two_children():
    check(
        11,
        "insert 2\ninsert 1\ninsert 3\ndelete 2\nexists 2\nnext 1\nprev 3\n",
        "false\n3\n1",
    )


def test_delete_root():
    check(
        11,
        "insert 5\ninsert 3\ninsert 7\ndelete 5\nexists 5\nnext 3\nprev 7\n",
        "false\n7\n3",
    )


def test_delete_all():
    check(
        11,
        "insert 1\ninsert 2\ninsert 3\n"
        "delete 1\ndelete 2\ndelete 3\n"
        "exists 1\nexists 2\nexists 3\n",
        "false\nfalse\nfalse",
    )


def test_negative_keys():
    check(
        11,
        "insert -5\ninsert -1\ninsert -10\n"
        "exists -5\nnext -10\nprev -1\n"
        "exists 0\nnext -1\n",
        "true\n-5\n-5\nfalse\nnone",
    )


def test_max_key_values():
    check(
        11,
        "insert 1000000000\ninsert -1000000000\n"
        "exists 1000000000\nexists -1000000000\n"
        "next 999999999\nprev -999999999\n"
        "next -1000000000\nprev 1000000000\n",
        "true\ntrue\n1000000000\n-1000000000\n1000000000\n-1000000000",
    )


def test_next_prev_none():
    check(
        11,
        "insert 5\nnext 5\nprev 5\nnext 10\nprev -10\n",
        "none\nnone\nnone\nnone",
    )


def test_ascending_insertion():
    n = 10_000
    lines = [f"insert {i}" for i in range(n)]
    lines.append(f"exists {n - 1}")
    lines.append(f"next {n - 2}")
    lines.append(f"prev {n - 1}")
    input_data = "\n".join(lines) + "\n"
    check(11, input_data, f"true\n{n - 1}\n{n - 2}")


def test_descending_insertion():
    n = 10_000
    lines = [f"insert {i}" for i in range(n - 1, -1, -1)]
    lines.append("exists 0")
    lines.append("next 0")
    lines.append("prev 1")
    input_data = "\n".join(lines) + "\n"
    check(11, input_data, f"true\n1\n0")


def test_interleaved_operations():
    check(
        11,
        "insert 10\n"
        "insert 5\n"
        "insert 15\n"
        "next 5\n"
        "prev 15\n"
        "delete 10\n"
        "next 5\n"
        "prev 15\n"
        "exists 10\n",
        "10\n10\n15\n5\nfalse",
    )
