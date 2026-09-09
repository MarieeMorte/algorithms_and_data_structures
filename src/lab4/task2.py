def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()

    s = s.replace(' ', '')
    n = len(s)

    if n < 3:
        with open('output.txt', 'w') as f:
            f.write('0')
        return

    total = [0] * 26
    for ch in s:
        total[ord(ch) - 97] += 1

    left = [0] * 26
    result = 0

    for ch in s:
        idx = ord(ch) - 97
        total[idx] -= 1

        for c in range(26):
            if left[c] and total[c]:
                result += left[c] * total[c]

        left[idx] += 1

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
