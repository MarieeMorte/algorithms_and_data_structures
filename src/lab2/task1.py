def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    keys = [0] * n
    left = [0] * n
    right = [0] * n

    for i in range(n):
        parts = lines[i + 1].strip().split()
        keys[i] = int(parts[0])
        left[i] = int(parts[1])
        right[i] = int(parts[2])

    in_order = []
    stack = []
    current = 0
    while stack or current != -1:
        if current != -1:
            stack.append(current)
            current = left[current]
        else:
            current = stack.pop()
            in_order.append(str(keys[current]))
            current = right[current]

    pre_order = []
    stack = [0]
    while stack:
        current = stack.pop()
        pre_order.append(str(keys[current]))
        if right[current] != -1:
            stack.append(right[current])
        if left[current] != -1:
            stack.append(left[current])

    post_order = []
    stack = [(0, False)]
    while stack:
        current, processed = stack.pop()
        if processed:
            post_order.append(str(keys[current]))
        else:
            stack.append((current, True))
            if right[current] != -1:
                stack.append((right[current], False))
            if left[current] != -1:
                stack.append((left[current], False))

    with open('output.txt', 'w') as f:
        f.write(' '.join(in_order) + '\n')
        f.write(' '.join(pre_order) + '\n')
        f.write(' '.join(post_order) + '\n')


if __name__ == '__main__':
    main()
