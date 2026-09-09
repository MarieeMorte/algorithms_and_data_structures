def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())

    if n == 0:
        with open('output.txt', 'w') as f:
            f.write('CORRECT\n')
        return

    keys = [0] * n
    left = [0] * n
    right = [0] * n

    for i in range(n):
        parts = lines[i + 1].strip().split()
        keys[i] = int(parts[0])
        left[i] = int(parts[1])
        right[i] = int(parts[2])

    def is_valid(node, min_key, max_key):
        if node == -1:
            return True

        key = keys[node]

        if key < min_key or key > max_key:
            return False

        return (is_valid(left[node], min_key, key - 1) and
                is_valid(right[node], key, max_key))

    result = is_valid(0, -2 ** 31, 2 ** 31 - 1)

    with open('output.txt', 'w') as f:
        f.write('CORRECT\n' if result else 'INCORRECT\n')


if __name__ == '__main__':
    solve()
