def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()

    n = len(s)
    dp = [0] * (n + 1)
    choice_len = [0] * (n + 1)
    choice_rep = [1] * (n + 1)

    for i in range(n - 1, -1, -1):
        best = 1 + dp[i + 1]
        best_len = 1
        best_rep = 1

        sub = s[i:]
        m = len(sub)
        z = [0] * m
        l, r = 0, 0
        for j in range(1, m):
            if j <= r:
                z[j] = min(r - j + 1, z[j - l])
            while j + z[j] < m and sub[z[j]] == sub[j + z[j]]:
                z[j] += 1
            if j + z[j] - 1 > r:
                l = j
                r = j + z[j] - 1

        for length in range(2, m + 1):
            cost = length + dp[i + length]
            if cost <= best:
                best = cost
                best_len = length
                best_rep = 1

        for length in range(1, m + 1):
            repeat = 1
            pos = length
            while pos + length <= m and z[pos] >= length:
                repeat += 1
                pos += length

            if repeat >= 2:
                cost = length + 1 + len(str(repeat)) + dp[i + length * repeat]
                if cost < best:
                    best = cost
                    best_len = length
                    best_rep = repeat

        dp[i] = best
        choice_len[i] = best_len
        choice_rep[i] = best_rep

    result = []
    i = 0
    while i < n:
        length = choice_len[i]
        repeat = choice_rep[i]
        block = s[i:i + length]
        if repeat == 1:
            result.append(block)
        else:
            result.append(f"{block}*{repeat}")
        i += length * repeat

    with open('output.txt', 'w') as f:
        f.write('+'.join(result))


if __name__ == "__main__":
    solve()
