def solve_matrix_chain():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())

        dimensions = []
        for _ in range(n):
            rows, cols = map(int, f.readline().strip().split())
            dimensions.append((rows, cols))

    p = []
    for i in range(n):
        p.append(dimensions[i][0])
    p.append(dimensions[-1][1])

    dp = [[0] * n for _ in range(n)]
    split = [[-1] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = 10 ** 18

            for mid in range(i, j):
                cost = dp[i][mid] + dp[mid + 1][j] + p[i] * p[mid + 1] * p[j + 1]

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = mid

    def build_parentheses(left_idx, right_idx):
        if left_idx == right_idx:
            return "A"

        best_split = split[left_idx][right_idx]
        left = build_parentheses(left_idx, best_split)
        right = build_parentheses(best_split + 1, right_idx)

        return "(" + left + right + ")"

    result = build_parentheses(0, n - 1)

    with open('output.txt', 'w') as f:
        f.write(result)


if __name__ == "__main__":
    solve_matrix_chain()
