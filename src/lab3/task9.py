def solve_negative_cycle():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    edges = []

    for i in range(1, m + 1):
        parts = lines[i].split()
        u = int(parts[0]) - 1
        v = int(parts[1]) - 1
        w = int(parts[2])
        edges.append((u, v, w))

    INF = 10 ** 18
    dist = [INF] * n
    dist[0] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            with open('output.txt', 'w') as f:
                f.write('1\n')
            return

    with open('output.txt', 'w') as f:
        f.write('0\n')


if __name__ == "__main__":
    solve_negative_cycle()
