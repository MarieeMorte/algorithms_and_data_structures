def solve():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    mod1 = 10 ** 9 + 7
    mod2 = 10 ** 9 + 9
    base = 911382323

    results = []

    for line in lines:
        if not line.strip():
            continue
        parts = line.split()
        k = int(parts[0])
        t = parts[1]
        p = parts[2]

        nt = len(t)
        np = len(p)

        if np > nt:
            results.append("0")
            continue

        max_len = max(nt, np) + 1
        pow1 = [1] * max_len
        pow2 = [1] * max_len
        for i in range(1, max_len):
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2

        ht1 = [0] * (nt + 1)
        ht2 = [0] * (nt + 1)
        for i in range(nt):
            ht1[i + 1] = (ht1[i] * base + ord(t[i])) % mod1
            ht2[i + 1] = (ht2[i] * base + ord(t[i])) % mod2

        hp1 = [0] * (np + 1)
        hp2 = [0] * (np + 1)
        for i in range(np):
            hp1[i + 1] = (hp1[i] * base + ord(p[i])) % mod1
            hp2[i + 1] = (hp2[i] * base + ord(p[i])) % mod2

        def get_hash_t(l, r):
            h1 = (ht1[r] - ht1[l] * pow1[r - l]) % mod1
            h2 = (ht2[r] - ht2[l] * pow2[r - l]) % mod2
            return h1, h2

        def get_hash_p(l, r):
            h1 = (hp1[r] - hp1[l] * pow1[r - l]) % mod1
            h2 = (hp2[r] - hp2[l] * pow2[r - l]) % mod2
            return h1, h2

        positions = []

        for i in range(nt - np + 1):
            mismatches = 0
            pos = 0

            while pos < np:
                lo, hi = 0, np - pos
                best = 0
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if mid == 0:
                        lo = mid + 1
                        continue
                    if get_hash_t(i + pos, i + pos + mid) == get_hash_p(pos, pos + mid):
                        best = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                pos += best

                if pos < np:
                    mismatches += 1
                    if mismatches > k:
                        break
                    pos += 1

            if mismatches <= k:
                positions.append(i)

        output_line = str(len(positions))
        if positions:
            output_line += ' ' + ' '.join(map(str, positions))
        results.append(output_line)

    with open('output.txt', 'w') as f:
        f.write('\n'.join(results))


if __name__ == "__main__":
    solve()
