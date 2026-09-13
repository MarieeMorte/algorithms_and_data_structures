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
        if len(parts) < 2:
            continue
        s, t = parts[0], parts[1]

        ns = len(s)
        nt = len(t)

        max_len = max(ns, nt) + 1
        pow1 = [1] * max_len
        pow2 = [1] * max_len
        for i in range(1, max_len):
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2

        hs1 = [0] * (ns + 1)
        hs2 = [0] * (ns + 1)
        for i in range(ns):
            hs1[i + 1] = (hs1[i] * base + ord(s[i])) % mod1
            hs2[i + 1] = (hs2[i] * base + ord(s[i])) % mod2

        ht1 = [0] * (nt + 1)
        ht2 = [0] * (nt + 1)
        for i in range(nt):
            ht1[i + 1] = (ht1[i] * base + ord(t[i])) % mod1
            ht2[i + 1] = (ht2[i] * base + ord(t[i])) % mod2

        def get_hash_s(l, r):
            h1 = (hs1[r] - hs1[l] * pow1[r - l]) % mod1
            h2 = (hs2[r] - hs2[l] * pow2[r - l]) % mod2
            return h1, h2

        def get_hash_t(l, r):
            h1 = (ht1[r] - ht1[l] * pow1[r - l]) % mod1
            h2 = (ht2[r] - ht2[l] * pow2[r - l]) % mod2
            return h1, h2

        def check(k):
            if k == 0:
                return 0, 0
            seen = {}
            for i in range(ns - k + 1):
                h = get_hash_s(i, i + k)
                if h not in seen:
                    seen[h] = i
            for j in range(nt - k + 1):
                h = get_hash_t(j, j + k)
                if h in seen:
                    return seen[h], j
            return None

        lo, hi = 0, min(ns, nt)
        best = (0, 0, 0)

        while lo <= hi:
            mid = (lo + hi) // 2
            res = check(mid)
            if res is not None:
                best = (res[0], res[1], mid)
                lo = mid + 1
            else:
                hi = mid - 1

        results.append(f"{best[0]} {best[1]} {best[2]}")

    with open('output.txt', 'w') as f:
        f.write('\n'.join(results))


if __name__ == "__main__":
    solve()
