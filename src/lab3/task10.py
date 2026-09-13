def solve_optimal_exchange():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    edges = []
    graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        parts = lines[i].split()
        u = int(parts[0]) - 1
        v = int(parts[1]) - 1
        w = int(parts[2])
        edges.append((u, v, w))
        graph[u].append(v)

    s = int(lines[m + 1]) - 1

    inf = 10 ** 18
    dist = [inf] * n
    dist[s] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    negative = [False] * n

    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                negative[v] = True
            if negative[u]:
                negative[v] = True

    with open('output.txt', 'w') as f:
        for i in range(n):
            if dist[i] == inf:
                visited = [False] * n
                stack = [s]
                visited[s] = True
                while stack:
                    vertex = stack.pop()
                    for neighbor in graph[vertex]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

                if not visited[i]:
                    f.write('*\n')
                else:
                    f.write('-\n')
            elif negative[i]:
                f.write('-\n')
            else:
                f.write(str(dist[i]) + '\n')


if __name__ == "__main__":
    solve_optimal_exchange()
