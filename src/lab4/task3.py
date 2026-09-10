def solve():
    with open('input.txt', 'r') as f:
        pattern = f.readline().strip()
        text = f.readline().strip()

    n = len(pattern)
    m = len(text)

    if n > m:
        with open('output.txt', 'w') as f:
            f.write('0\n\n')
        return

    mod = 10 ** 9 + 7
    base = 911382323

    pow_base = [1] * (m + 1)
    for i in range(1, m + 1):
        pow_base[i] = (pow_base[i - 1] * base) % mod

    pattern_hash = 0
    for ch in pattern:
        pattern_hash = (pattern_hash * base + ord(ch)) % mod

    text_hash = [0] * (m + 1)
    for i in range(m):
        text_hash[i + 1] = (text_hash[i] * base + ord(text[i])) % mod

    positions = []

    for i in range(m - n + 1):
        hash_sub = (text_hash[i + n] - text_hash[i] * pow_base[n]) % mod

        if hash_sub == pattern_hash:
            if text[i:i + n] == pattern:
                positions.append(i + 1)

    with open('output.txt', 'w') as f:
        f.write(str(len(positions)) + '\n')
        if positions:
            f.write(' '.join(map(str, positions)))
        else:
            f.write('')


if __name__ == "__main__":
    solve()
