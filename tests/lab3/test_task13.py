from test_utils import check


def test_minimal():
    check(13, "1 1\n#\n", "1")


def test_minimal_empty():
    check(13, "1 1\n.\n", "0")


def test_example_1():
    check(13,
          "5 10\n"
          "##......#.\n"
          ".#..#...#.\n"
          ".###....#.\n"
          "..##....#.\n"
          "........#.\n",
          "3")


def test_example_2():
    check(13,
          "5 10\n"
          "##..#####.\n"
          ".#.#.#....\n"
          "###..##.#.\n"
          "..##.....#\n"
          ".###.#####\n",
          "5")


def test_maximal():
    n = 200
    m = 200
    lines = [f"{n} {m}"]
    for _ in range(n):
        lines.append("#" * m)
    check(13, "\n".join(lines) + "\n", "1")


def test_maximal_empty():
    n = 200
    m = 200
    lines = [f"{n} {m}"]
    for _ in range(n):
        lines.append("." * m)
    check(13, "\n".join(lines) + "\n", "0")


def test_maximal_checkerboard():
    # Каждая # изолирована (только угловые касания - не считаются)
    n = 200
    m = 200
    lines = [f"{n} {m}"]
    for i in range(n):
        row = ""
        for j in range(m):
            row += "#" if (i + j) % 2 == 0 else "."
        lines.append(row)
    check(13, "\n".join(lines) + "\n", str(n * m // 2))


def test_single_row():
    check(13, "1 5\n#.#.#\n", "3")


def test_single_column():
    check(13, "5 1\n#\n.\n#\n.\n#\n", "3")


def test_full_row():
    check(13, "1 5\n#####\n", "1")


def test_diagonal_touch():
    # Угловое касание не считается соединением
    check(13, "2 2\n#.\n.#\n", "2")


def test_l_shape():
    check(13, "3 3\n#..\n#..\n###\n", "1")


def test_two_separate():
    check(13, "3 5\n#...#\n#...#\n#####\n", "1")


def test_all_dots():
    check(13, "3 3\n...\n...\n...\n", "0")


def test_all_hashes():
    check(13, "3 3\n###\n###\n###\n", "1")


def test_multiple_beds():
    check(13,
          "5 5\n"
          "##...\n"
          "##...\n"
          ".....\n"
          "...##\n"
          "...##\n",
          "2")
