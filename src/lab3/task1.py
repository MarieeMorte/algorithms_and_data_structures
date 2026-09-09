from collections import deque


def solve_labyrinth():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    n, m = map(int, lines[0].strip().split())

    graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        u, v = map(int, lines[i].strip().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    u, v = map(int, lines[m + 1].strip().split())
    u -= 1
    v -= 1

    visited = [False] * n
    queue = deque([u])
    visited[u] = True

    while queue:
        curr = queue.popleft()

        if curr == v:
            with open('output.txt', 'w') as f:
                f.write('1\n')
            return

        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    with open('output.txt', 'w') as f:
        f.write('0\n')


if __name__ == "__main__":
    solve_labyrinth()
