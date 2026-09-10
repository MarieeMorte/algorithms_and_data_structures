import random

from test_utils import check


def _evaluate(s, dims):
    pos = [0]
    mat_idx = [0]

    def parse():
        if s[pos[0]] == "A":
            pos[0] += 1
            a, b = dims[mat_idx[0]]
            mat_idx[0] += 1
            return a, b, 0
        pos[0] += 1
        a1, b1, c1 = parse()
        a2, b2, c2 = parse()
        pos[0] += 1
        return a1, b2, c1 + c2 + a1 * b1 * b2

    _, _, cost = parse()
    return cost


def _dp_cost(dims):
    n = len(dims)
    p = [dims[0][0]] + [b for _, b in dims]
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = min(
                dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                for k in range(i, j)
            )
    return dp[0][n - 1]


def _check_structure(s, n):
    assert s.count("A") == n, f"ожидалось {n} букв A, получено {s.count('A')}"
    assert s.count("(") == n - 1, f"ожидалось {n - 1} открывающих скобок"
    assert s.count(")") == n - 1, f"ожидалось {n - 1} закрывающих скобок"
    bal = 0
    for ch in s:
        if ch == "(":
            bal += 1
        elif ch == ")":
            bal -= 1
        assert bal >= 0, "отрицательный баланс скобок"
    assert bal == 0, "несбалансированные скобки"


def _make_input(dims):
    return f"{len(dims)}\n" + "\n".join(f"{a} {b}" for a, b in dims) + "\n"


def test_minimal():
    check(19, "1\n10 20\n", "A")


def test_example():
    check(19, "3\n10 50\n50 90\n90 20\n", "((AA)A)")


def test_maximal():
    n = 400
    dims = [(100, 100)] * n
    output = check(19, _make_input(dims), timeout=60)
    _check_structure(output, n)


def test_two_matrices():
    check(19, "2\n5 10\n10 7\n", "(AA)")


def test_identical_matrices():
    n = 4
    dims = [(7, 7)] * n
    output = check(19, _make_input(dims))
    _check_structure(output, n)
    cost = _evaluate(output, dims)
    assert cost == _dp_cost(dims)


def test_optimality_fixed():
    dims = [(5, 10), (10, 3), (3, 7)]
    output = check(19, _make_input(dims))
    _check_structure(output, 3)
    cost = _evaluate(output, dims)
    assert cost == 255
    assert cost == _dp_cost(dims)


def test_optimality_n4():
    dims = [(10, 20), (20, 30), (30, 40), (40, 50)]
    output = check(19, _make_input(dims))
    _check_structure(output, 4)
    cost = _evaluate(output, dims)
    assert cost == _dp_cost(dims)


def test_large_values():
    dims = [(100, 100)] * 3
    output = check(19, _make_input(dims))
    _check_structure(output, 3)
    cost = _evaluate(output, dims)
    assert cost == 2 * 100 * 100 * 100


def test_stress_random_small():
    random.seed(19)
    for trial in range(15):
        n = random.randint(1, 7)
        dims = []
        a = random.randint(1, 20)
        for _ in range(n):
            b = random.randint(1, 20)
            dims.append((a, b))
            a = b

        input_data = _make_input(dims)
        output = check(19, input_data)
        _check_structure(output, n)

        cost = _evaluate(output, dims)
        expected = _dp_cost(dims)
        assert cost == expected, (
            f"trial #{trial}: dims={dims}, cost={cost}, expected={expected}"
        )
