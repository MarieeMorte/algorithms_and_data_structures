def solve_souvenirs():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        values = list(map(int, f.readline().strip().split()))

    total_sum = sum(values)

    if total_sum % 3 != 0:
        result = 0
    else:
        target = total_sum // 3

        dp = [[False] * (target + 1) for _ in range(target + 1)]
        dp[0][0] = True

        for value in values:
            for s1 in range(target, -1, -1):
                for s2 in range(target, -1, -1):
                    if dp[s1][s2]:
                        if s1 + value <= target:
                            dp[s1 + value][s2] = True
                        if s2 + value <= target:
                            dp[s1][s2 + value] = True

        result = 1 if dp[target][target] else 0

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve_souvenirs()
