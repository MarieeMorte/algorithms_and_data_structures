def solve():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()

    n = len(s)

    if len(t) != n:
        result = -1
    else:
        doubled = s + s
        best_x = -1
        start = 0
        while True:
            pos = doubled.find(t, start)
            if pos == -1 or pos >= n:
                break
            x = (n - pos) % n
            if best_x == -1 or x < best_x:
                best_x = x
            start = pos + 1

        result = best_x

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
