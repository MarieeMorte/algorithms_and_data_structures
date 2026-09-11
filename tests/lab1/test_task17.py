from test_utils import check

MOD = 10 ** 9

MOVES = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}


def test_minimal():
    check(17, "1\n", "8")


def test_example_1():
    check(17, "1\n", "8")


def test_example_2():
    check(17, "2\n", "16")


def test_maximal():
    output = check(17, "1000\n", timeout=30)
    value = int(output)
    assert 0 <= value < MOD
    assert value == _reference(1000)


def test_n3():
    check(17, "3\n", "36")


def test_n4():
    check(17, "4\n", "82")


def test_n5():
    check(17, "5\n", "188")


def test_n6():
    check(17, "6\n", "428")


def test_mod_stable_large():
    output = check(17, "500\n", timeout=30)
    value = int(output)
    assert 0 <= value < MOD


def test_no_start_with_zero_or_eight():
    # Если бы 0 или 8 были разрешены как стартовые, для n=1 было бы 10
    check(17, "1\n", "8")


def _count_from(start, remaining):
    if remaining == 1:
        return 1
    return sum(_count_from(nxt, remaining - 1) for nxt in MOVES[start])


def _brute_force(n):
    starts = [d for d in range(10) if d != 0 and d != 8]
    return sum(_count_from(s, n) for s in starts) % MOD


def _reference(n):
    dp = [0] * 10
    for d in range(10):
        if d != 0 and d != 8:
            dp[d] = 1
    for _ in range(2, n + 1):
        new_dp = [0] * 10
        for d in range(10):
            for prev in MOVES[d]:
                new_dp[d] = (new_dp[d] + dp[prev]) % MOD
        dp = new_dp
    return sum(dp) % MOD


def test_stress_random_small():
    for n in range(1, 8):
        expected = _brute_force(n)
        got = int(check(17, f"{n}\n"))
        assert got == expected, (
            f"n={n}: expected={expected}, got={got}"
        )
