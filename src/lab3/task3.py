import sys

sys.setrecursionlimit(10000)


def solve_cycles():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    lines = [line.strip() for line in lines if line.strip()]

    n, m = map(int, lines[0].split())

    graph = [[] for _ in range(n)]

    for i in range(1, m + 1):
        parts = lines[i].split()
        if len(parts) >= 2:
            u = int(parts[0]) - 1
            v = int(parts[1]) - 1
            graph[u].append(v)

    visited = [False] * n
    rec_stack = [False] * n

    def dfs(vertex):
        visited[vertex] = True
        rec_stack[vertex] = True

        for neighbor in graph[vertex]:
            if not isinstance(neighbor, int):
                continue
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[vertex] = False
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i):
                with open('output.txt', 'w') as f:
                    f.write('1\n')
                return

    with open('output.txt', 'w') as f:
        f.write('0\n')


if __name__ == "__main__":
    solve_cycles()
