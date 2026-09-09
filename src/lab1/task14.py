def solve_max_arithmetic_expression():
    with open('input.txt', 'r') as f:
        expression = f.readline().strip()

    numbers = []
    operations = []

    for i, char in enumerate(expression):
        if i % 2 == 0:
            numbers.append(int(char))
        else:
            operations.append(char)

    n = len(numbers)

    dp_min = [[float('inf')] * n for _ in range(n)]
    dp_max = [[-float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp_min[i][i] = numbers[i]
        dp_max[i][i] = numbers[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            for k in range(i, j):
                op = operations[k]

                left_min = dp_min[i][k]
                left_max = dp_max[i][k]
                right_min = dp_min[k + 1][j]
                right_max = dp_max[k + 1][j]

                results = []
                if op == '+':
                    results = [
                        left_min + right_min,
                        left_min + right_max,
                        left_max + right_min,
                        left_max + right_max
                    ]
                elif op == '-':
                    results = [
                        left_min - right_min,
                        left_min - right_max,
                        left_max - right_min,
                        left_max - right_max
                    ]
                elif op == '*':
                    results = [
                        left_min * right_min,
                        left_min * right_max,
                        left_max * right_min,
                        left_max * right_max
                    ]

                dp_min[i][j] = min(dp_min[i][j], min(results))
                dp_max[i][j] = max(dp_max[i][j], max(results))

    result = dp_max[0][n - 1]

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve_max_arithmetic_expression()
