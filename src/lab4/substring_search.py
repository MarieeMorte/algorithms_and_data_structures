def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()

    n = len(s)
    m = len(t)

    if m > n:
        with open('output.txt', 'w') as f:
            f.write('')
        return

    combined = t + '#' + s
    pi = [0] * len(combined)

    for i in range(1, len(combined)):
        j = pi[i - 1]
        while j > 0 and combined[i] != combined[j]:
            j = pi[j - 1]
        if combined[i] == combined[j]:
            j += 1
        pi[i] = j

    positions = []
    for i in range(m + 1, len(combined)):
        if pi[i] == m:
            positions.append(i - 2 * m)

    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, positions)))


if __name__ == "__main__":
    solve()
