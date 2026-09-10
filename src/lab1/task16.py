def solve_tsp():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())

        dist = []
        for _ in range(n):
            row = list(map(int, f.readline().strip().split()))
            dist.append(row)

    inf = float('inf')
    dp = [[inf] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    for i in range(n):
        dp[1 << i][i] = 0

    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == inf:
                continue

            for next_city in range(n):
                if mask & (1 << next_city):
                    continue

                new_mask = mask | (1 << next_city)
                new_dist = dp[mask][last] + dist[last][next_city]

                if new_dist < dp[new_mask][next_city]:
                    dp[new_mask][next_city] = new_dist
                    parent[new_mask][next_city] = last

    full_mask = (1 << n) - 1
    best_dist = inf
    best_last = -1

    for last in range(n):
        if dp[full_mask][last] < best_dist:
            best_dist = dp[full_mask][last]
            best_last = last

    path = []
    mask = full_mask
    last = best_last

    while last != -1:
        path.append(last + 1)
        prev = parent[mask][last]
        mask = mask ^ (1 << last)
        last = prev

    path.reverse()

    with open('output.txt', 'w') as f:
        f.write(str(best_dist) + '\n')
        f.write(' '.join(map(str, path)))

        if len(path) > 0:
            f.write(' ')


if __name__ == "__main__":
    solve_tsp()
