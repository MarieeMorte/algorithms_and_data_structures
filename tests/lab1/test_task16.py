import itertools
import random

from test_utils import check


def _parse(output):
    lines = output.strip().split("\n")
    length = int(lines[0].strip())
    path = list(map(int, lines[1].split()))
    return length, path


def _path_length(dist, path):
    return sum(dist[path[i] - 1][path[i + 1] - 1] for i in range(len(path) - 1))


def test_minimal():
    output = check(16, "1\n0\n")
    length, path = _parse(output)
    assert length == 0
    assert path == [1]


def test_example():
    input_data = (
        "5\n"
        "0 183 163 173 181\n"
        "183 0 165 172 171\n"
        "163 165 0 189 302\n"
        "173 172 189 0 167\n"
        "181 171 302 167 0\n"
    )
    output = check(16, input_data)
    length, path = _parse(output)
    assert length == 666
    assert sorted(path) == [1, 2, 3, 4, 5]


def test_maximal():
    random.seed(16)
    n = 13
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = random.randint(1, 10 ** 6)
            mat[i][j] = d
            mat[j][i] = d

    lines = [str(n)] + [" ".join(map(str, row)) for row in mat]
    input_data = "\n".join(lines) + "\n"

    output = check(16, input_data, timeout=60)
    length, path = _parse(output)

    assert sorted(path) == list(range(1, n + 1))
    assert _path_length(mat, path) == length
    assert length == _dp_reference(mat, n)


def test_two_cities():
    output = check(16, "2\n0 5\n5 0\n")
    length, path = _parse(output)
    assert length == 5
    assert sorted(path) == [1, 2]


def test_any_start():
    mat = [
        [0, 1, 10],
        [1, 0, 100],
        [10, 100, 0],
    ]
    lines = ["3"] + [" ".join(map(str, row)) for row in mat]
    output = check(16, "\n".join(lines) + "\n")
    length, path = _parse(output)
    assert length == 11
    assert sorted(path) == [1, 2, 3]
    assert _path_length(mat, path) == 11


def test_all_zeros():
    n = 5
    mat = [[0] * n for _ in range(n)]
    lines = [str(n)] + [" ".join(map(str, row)) for row in mat]
    output = check(16, "\n".join(lines) + "\n")
    length, path = _parse(output)
    assert length == 0
    assert sorted(path) == list(range(1, n + 1))


def test_line_distances():
    mat = [
        [0, 1, 2, 3],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [3, 2, 1, 0],
    ]
    lines = ["4"] + [" ".join(map(str, row)) for row in mat]
    output = check(16, "\n".join(lines) + "\n")
    length, path = _parse(output)
    assert length == 3
    assert _path_length(mat, path) == 3


def test_equal_weights():
    mat = [
        [0, 7, 7, 7],
        [7, 0, 7, 7],
        [7, 7, 0, 7],
        [7, 7, 7, 0],
    ]
    lines = ["4"] + [" ".join(map(str, row)) for row in mat]
    output = check(16, "\n".join(lines) + "\n")
    length, path = _parse(output)
    assert length == 21
    assert sorted(path) == [1, 2, 3, 4]


def test_big_values():
    mat = [
        [0, 10 ** 6, 10 ** 6],
        [10 ** 6, 0, 10 ** 6],
        [10 ** 6, 10 ** 6, 0],
    ]
    lines = ["3"] + [" ".join(map(str, row)) for row in mat]
    output = check(16, "\n".join(lines) + "\n")
    length, path = _parse(output)
    assert length == 2 * 10 ** 6
    assert sorted(path) == [1, 2, 3]


def _dp_reference(dist, n):
    if n == 1:
        return 0
    INF = float('inf')
    full = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
    for mask in range(1 << n):
        for last in range(n):
            cur = dp[mask][last]
            if cur == INF:
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                cand = cur + dist[last][nxt]
                if cand < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = cand
    return min(dp[full][i] for i in range(n))


def _brute_force(dist, n):
    if n == 1:
        return 0
    best = None
    for perm in itertools.permutations(range(n)):
        length = sum(dist[perm[i]][perm[i + 1]] for i in range(n - 1))
        if best is None or length < best:
            best = length
    return best


def test_stress_random_small():
    random.seed(1616)
    for trial in range(20):
        n = random.randint(1, 7)
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                d = random.randint(0, 50)
                mat[i][j] = d
                mat[j][i] = d

        lines = [str(n)] + [" ".join(map(str, row)) for row in mat]
        input_data = "\n".join(lines) + "\n"

        expected = _brute_force(mat, n)
        output = check(16, input_data)
        length, path = _parse(output)

        assert sorted(path) == list(range(1, n + 1)), (
            f"trial #{trial}: path={path} not a permutation"
        )
        assert _path_length(mat, path) == length, (
            f"trial #{trial}: path length mismatch"
        )
        assert length == expected, (
            f"trial #{trial}: expected={expected}, got={length}"
        )
