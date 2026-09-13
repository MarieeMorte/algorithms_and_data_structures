def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())

    if n == 0:
        with open('output.txt', 'w') as f:
            f.write('YES\n')
        return

    keys = [0] * n
    left = [0] * n
    right = [0] * n

    for i in range(n):
        parts = lines[i + 1].strip().split()
        keys[i] = int(parts[0])
        left[i] = int(parts[1]) - 1
        right[i] = int(parts[2]) - 1

    stack = [(0, -10 ** 18, 10 ** 18)]

    while stack:
        node, min_key, max_key = stack.pop()

        if node == -1:
            continue

        key = keys[node]

        if key <= min_key or key >= max_key:
            with open('output.txt', 'w') as f:
                f.write('NO\n')
            return

        stack.append((left[node], min_key, key))

        stack.append((right[node], key, max_key))

    with open('output.txt', 'w') as f:
        f.write('YES\n')


if __name__ == '__main__':
    solve()
