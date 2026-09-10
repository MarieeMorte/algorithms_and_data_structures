def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()
        q = int(f.readline())

        n = len(s)

        mod1 = 10 ** 9 + 7
        mod2 = 10 ** 9 + 9
        base = 911382323

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i in range(n):
            h1[i + 1] = (h1[i] * base + ord(s[i])) % mod1
            h2[i + 1] = (h2[i] * base + ord(s[i])) % mod2

        results = []
        for _ in range(q):
            a, b, l = map(int, f.readline().split())

            hash1_a = (h1[a + l] - h1[a] * pow1[l]) % mod1
            hash2_a = (h2[a + l] - h2[a] * pow2[l]) % mod2

            hash1_b = (h1[b + l] - h1[b] * pow1[l]) % mod1
            hash2_b = (h2[b + l] - h2[b] * pow2[l]) % mod2

            if hash1_a == hash1_b and hash2_a == hash2_b:
                results.append("Yes")
            else:
                results.append("No")

    with open('output.txt', 'w') as f:
        f.write('\n'.join(results))


if __name__ == "__main__":
    solve()
