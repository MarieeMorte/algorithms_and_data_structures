import math


def solve_mst():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())
    points = []

    for i in range(1, n + 1):
        x, y = map(int, lines[i].strip().split())
        points.append((x, y))

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            weight = math.sqrt(dx * dx + dy * dy)
            edges.append((weight, i, j))

    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    total_weight = 0.0
    edges_used = 0

    for weight, u, v in edges:
        if union(u, v):
            total_weight += weight
            edges_used += 1
            if edges_used == n - 1:
                break

    with open('output.txt', 'w') as f:
        f.write(f'{total_weight:.9f}\n')


if __name__ == "__main__":
    solve_mst()
