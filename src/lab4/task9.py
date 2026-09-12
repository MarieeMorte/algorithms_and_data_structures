def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()

    n = len(s)

    if n == 0:
        with open('output.txt', 'w') as f:
            f.write('')
        return

    l_max = 20

    runs = [[1] * (n + 1) for _ in range(l_max + 1)]

    for L in range(1, l_max + 1):
        arr = runs[L]
        for i in range(n - 2 * L, -1, -1):
            if s[i:i + L] == s[i + L:i + 2 * L]:
                arr[i] = arr[i + L] + 1

    dp = [0] * (n + 1)
    choice_len = [0] * (n + 1)
    choice_rep = [1] * (n + 1)

    for i in range(n - 1, -1, -1):
        best = 1 + dp[i + 1]
        best_len = 1
        best_rep = 1

        max_len = min(n - i, best)

        for length in range(2, max_len + 1):
            cost = length + dp[i + length]
            if cost <= best:
                best = cost
                best_len = length
                best_rep = 1

        for length in range(1, max_len + 1):
            if length + 2 >= best:
                break

            if length <= l_max:
                repeat = runs[length][i]
            else:
                block = s[i:i + length]
                repeat = 1
                pos = i + length
                while pos + length <= n and s.startswith(block, pos):
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
