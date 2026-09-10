def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()

    n = len(s)

    if len(t) != n:
        result = -1
    else:
        doubled = s + s
        pos = doubled.find(t)

        if pos == -1 or pos >= n:
            result = -1
        else:
            result = (n - pos) % n

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
