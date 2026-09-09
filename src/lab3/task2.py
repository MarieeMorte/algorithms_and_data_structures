from collections import deque


def solve_components():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n, m = map(int, lines[0].strip().split())

    graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        if not lines[i].strip():
            continue
        u, v = map(int, lines[i].strip().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            vertex = queue.popleft()
            if not isinstance(vertex, int):
                continue
            for neighbor in graph[vertex]:
                if not isinstance(neighbor, int):
                    continue
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    components = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            components += 1

    with open('output.txt', 'w') as f:
        f.write(str(components) + '\n')


if __name__ == "__main__":
    solve_components()
