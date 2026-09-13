from test_utils import check


def test_minimal():
    check(17, "1\n? 0\n", "Not found")


def test_example_1():
    check(
        17,
        "15\n"
        "? 1\n"
        "+ 1\n"
        "? 1\n"
        "+ 2\n"
        "s 1 2\n"
        "+ 1000000000\n"
        "? 1000000000\n"
        "- 1000000000\n"
        "? 1000000000\n"
        "s 999999999 1000000000\n"
        "- 2\n"
        "? 2\n"
        "- 0\n"
        "+ 9\n"
        "s 0 9\n",
        "Not found\n"
        "Found\n"
        "3\n"
        "Found\n"
        "Not found\n"
        "1\n"
        "Not found\n"
        "10",
    )


def test_example_2():
    check(
        17,
        "5\n"
        "? 0\n"
        "+ 0\n"
        "? 0\n"
        "- 0\n"
        "? 0\n",
        "Not found\nFound\nNot found",
    )


def test_example_3():
    check(
        17,
        "5\n"
        "+ 491572259\n"
        "? 491572259\n"
        "? 899375874\n"
        "s 310971296 877523306\n"
        "+ 352411209\n",
        "Found\nNot found\n491572259",
    )


def test_maximum():
    n = 100_000
    lines = [str(n)]
    for i in range(1, n):
        lines.append(f"+ {i}")
    lines.append(f"s 1 {n - 1}")
    input_data = "\n".join(lines) + "\n"
    expected = str((n - 1) * n // 2)
    check(17, input_data, expected, timeout=60)


def test_find_empty():
    check(17, "1\n? 5\n", "Not found")


def test_add_find():
    check(17, "2\n+ 5\n? 5\n", "Found")


def test_delete():
    check(17, "3\n+ 5\n- 5\n? 5\n", "Not found")


def test_sum_empty():
    check(17, "1\ns 1 10\n", "0")


def test_sum_range():
    check(17, "4\n+ 1\n+ 3\n+ 5\ns 2 4\n", "3")


def test_online_dependency():
    check(
        17,
        "5\n"
        "+ 1\n"
        "s 1 1\n"
        "+ 1\n"
        "? 2\n"
        "? 1\n",
        "1\nNot found\nFound",
    )


def test_boundary():
    check(
        17,
        "4\n"
        "+ 1000000000\n"
        "? 1000000000\n"
        "s 1000000000 1000000000\n"
        "? 0\n",
        "Found\n1000000000\nFound",
    )


def test_max_key():
    check(
        17,
        "4\n"
        "+ 999999999\n"
        "+ 1000000000\n"
        "s 999999999 1000000000\n"
        "? 0\n",
        "1999999999\nNot found",
    )


def test_duplicates():
    check(17, "3\n+ 5\n+ 5\n? 5\n", "Found")


def test_delete_nonexistent():
    check(17, "4\n- 5\n? 5\n+ 5\n? 5\n", "Not found\nFound")


def test_add_delete_add():
    check(
        17,
        "6\n"
        "+ 10\n"
        "- 10\n"
        "+ 20\n"
        "? 10\n"
        "? 20\n"
        "s 10 20\n",
        "Not found\nFound\n20",
    )


def test_online_with_multiple_sums():
    check(
        17,
        "7\n"
        "+ 5\n"
        "s 1 10\n"
        "+ 2\n"
        "s 1 10\n"
        "+ 3\n"
        "? 5\n"
        "? 0\n",
        "5\n7\nNot found\nFound",
    )


def test_zero_handling():
    check(
        17,
        "5\n"
        "+ 0\n"
        "? 0\n"
        "s 0 0\n"
        "- 0\n"
        "? 0\n",
        "Found\n0\nNot found",
    )
