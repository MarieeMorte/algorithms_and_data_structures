def solve_knight_moves():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())

    mod = 10 ** 9

    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    dp = [0] * 10

    for digit in range(10):
        if digit != 0 and digit != 8:
            dp[digit] = 1

    for _ in range(2, n + 1):
        new_dp = [0] * 10

        for digit in range(10):
            for prev_digit in moves[digit]:
                new_dp[digit] = (new_dp[digit] + dp[prev_digit]) % mod

        dp = new_dp

    result = sum(dp) % mod

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve_knight_moves()
