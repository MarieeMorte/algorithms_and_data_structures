def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())

    if n == 0:
        with open('output.txt', 'w') as f:
            f.write('0\n')
        return

    left = [0] * n
    right = [0] * n

    for i in range(n):
        parts = lines[i + 1].strip().split()
        left[i] = int(parts[1]) - 1
        right[i] = int(parts[2]) - 1

    stack = [(0, 1)]
    max_height = 0

    while stack:
        node, depth = stack.pop()

        if node == -1:
            continue

        max_height = max(max_height, depth)

        if left[node] != -1:
            stack.append((left[node], depth + 1))
        if right[node] != -1:
            stack.append((right[node], depth + 1))

    with open('output.txt', 'w') as f:
        f.write(str(max_height) + '\n')


if __name__ == '__main__':
    solve()
