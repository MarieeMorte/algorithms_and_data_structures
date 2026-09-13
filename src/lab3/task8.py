import heapq


def solve_shortest_path():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        parts = lines[i].split()
        u = int(parts[0]) - 1
        v = int(parts[1]) - 1
        w = int(parts[2])
        graph[u].append((v, w))

    u, v = map(int, lines[m + 1].split())
    u -= 1
    v -= 1

    inf = 10 ** 18
    dist = [inf] * n
    dist[u] = 0
    pq = [(0, u)]

    while pq:
        d, vertex = heapq.heappop(pq)

        if d > dist[vertex]:
            continue

        if vertex == v:
            break

        for neighbor, weight in graph[vertex]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    with open('output.txt', 'w') as f:
        if dist[v] == inf:
            f.write('-1\n')
        else:
            f.write(str(dist[v]) + '\n')


if __name__ == "__main__":
    solve_shortest_path()
