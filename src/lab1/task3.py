def solve_max_advertising_revenue():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())

        a = []
        while len(a) < n:
            a.extend(map(int, f.readline().strip().split()))

        b = []
        while len(b) < n:
            b.extend(map(int, f.readline().strip().split()))

    a.sort()
    b.sort()

    total_revenue = sum(a[i] * b[i] for i in range(n))

    with open('output.txt', 'w') as f:
        f.write(str(total_revenue))


if __name__ == "__main__":
    solve_max_advertising_revenue()
