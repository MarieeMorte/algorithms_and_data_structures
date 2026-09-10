def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()

    n = len(s)

    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    period = n - pi[n - 1]

    result = period

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
