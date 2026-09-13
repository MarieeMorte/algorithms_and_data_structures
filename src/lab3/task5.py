from typing import List, Tuple


def solve_scc():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    graph: List[List[int]] = [[] for _ in range(n)]
    rev_graph: List[List[int]] = [[] for _ in range(n)]

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append(v)
        rev_graph[v].append(u)

    visited: List[bool] = [False] * n
    order: List[int] = []

    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        dfs_stack: List[Tuple[int, int]] = [(start, 0)]
        while dfs_stack:
            vertex, idx = dfs_stack[-1]
            if idx < len(graph[vertex]):
                neighbor = graph[vertex][idx]
                dfs_stack[-1] = (vertex, idx + 1)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs_stack.append((neighbor, 0))
            else:
                order.append(vertex)
                dfs_stack.pop()

    visited = [False] * n
    components = 0

    for start in reversed(order):
        if visited[start]:
            continue
        components += 1
        visited[start] = True
        walk_stack: List[int] = [start]
        while walk_stack:
            vertex = walk_stack.pop()
            for neighbor in rev_graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    walk_stack.append(neighbor)

    with open('output.txt', 'w') as f:
        f.write(str(components) + '\n')


if __name__ == "__main__":
    solve_scc()
