def solve():
    with open('input.txt', 'r') as f:
        p = f.readline().strip()
        t = f.readline().strip()

    n = len(p)
    m = len(t)
    positions = []

    for i in range(m - n + 1):
        match = True
        for j in range(n):
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            positions.append(i + 1)

    with open('output.txt', 'w') as f:
        f.write(str(len(positions)) + '\n')
        if positions:
            f.write(' '.join(map(str, positions)))
        else:
            f.write('')


if __name__ == "__main__":
    solve()
