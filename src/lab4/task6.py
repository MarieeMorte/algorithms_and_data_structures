def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()

    n = len(s)
    z = [0] * n

    l = 0
    r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, z[1:])))


if __name__ == "__main__":
    solve()
