def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())

    if n == 0:
        return

    left = [0] * n
    right = [0] * n

    for i in range(n):
        parts = lines[i + 1].strip().split()
        left[i] = int(parts[1]) - 1
        right[i] = int(parts[2]) - 1

    heights = [0] * n
    balances = [0] * n

    stack = [(0, False)]

    while stack:
        node, processed = stack.pop()

        if node == -1:
            continue

        if processed:
            left_height = heights[left[node]] if left[node] != -1 else 0
            right_height = heights[right[node]] if right[node] != -1 else 0

            heights[node] = 1 + max(left_height, right_height)

            balances[node] = right_height - left_height
        else:
            stack.append((node, True))

            if right[node] != -1:
                stack.append((right[node], False))
            if left[node] != -1:
                stack.append((left[node], False))

    with open('output.txt', 'w') as f:
        for i in range(n):
            f.write(str(balances[i]) + '\n')


if __name__ == '__main__':
    solve()
