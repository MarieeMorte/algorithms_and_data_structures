def solve_garden():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n, m = map(int, lines[0].split())
    grid = [list(lines[i].strip()) for i in range(1, n + 1)]

    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and not visited[i][j]:
                count += 1
                visited[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '#':
                            visited[nx][ny] = True
                            stack.append((nx, ny))

    with open('output.txt', 'w') as f:
        f.write(str(count) + '\n')


if __name__ == "__main__":
    solve_garden()
