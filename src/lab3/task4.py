from collections import deque
from typing import List


def solve_topological_sort():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    graph: List[List[int]] = [[] for _ in range(n)]
    in_degree: List[int] = [0] * n

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        u -= 1
        v -= 1
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    order: List[int] = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    with open('output.txt', 'w') as f:
        f.write(' '.join(str(v + 1) for v in order) + '\n')


if __name__ == "__main__":
    solve_topological_sort()
