def solve_topological_sort():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append(v)

    visited = [False] * n
    order = []

    def dfs(vertex):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if isinstance(neighbor, int) and not visited[neighbor]:
                dfs(neighbor)
        order.append(vertex)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    with open('output.txt', 'w') as f:
        f.write(' '.join(str(v + 1) for v in reversed(order)) + '\n')


if __name__ == "__main__":
    solve_topological_sort()
