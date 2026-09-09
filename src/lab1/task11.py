def solve_knapsack():
    with open('input.txt', 'r') as f:
        first_line = f.readline().strip()
        while first_line == '':
            first_line = f.readline().strip()
        capacity, n = map(int, first_line.split())

        weights = []
        while len(weights) < n:
            weights.extend(map(int, f.readline().strip().split()))

    dp = [0] * (capacity + 1)

    for weight in weights:
        if weight == 0:
            continue
        for w in range(capacity, weight - 1, -1):
            if dp[w - weight] + weight > dp[w]:
                dp[w] = dp[w - weight] + weight

    max_weight = dp[capacity]

    with open('output.txt', 'w') as f:
        f.write(str(max_weight))


if __name__ == "__main__":
    solve_knapsack()
