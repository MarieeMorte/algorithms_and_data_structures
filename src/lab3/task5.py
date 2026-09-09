def solve_scc():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append(v)
        rev_graph[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(vertex):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if isinstance(neighbor, int) and not visited[neighbor]:
                dfs1(neighbor)
        order.append(vertex)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    components = 0

    def dfs2(vertex):
        visited[vertex] = True
        for neighbor in rev_graph[vertex]:
            if isinstance(neighbor, int) and not visited[neighbor]:
                dfs2(neighbor)

    for i in reversed(order):
        if not visited[i]:
            dfs2(i)
            components += 1

    with open('output.txt', 'w') as f:
        f.write(str(components) + '\n')


if __name__ == "__main__":
    solve_scc()
