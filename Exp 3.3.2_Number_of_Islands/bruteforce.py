
def num_islands_brute_force(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= m or c < 0 or c >= n):
            return

        if visited[r][c] or grid[r][c] == '0':
            return

        visited[r][c] = True

        # Explore up, down, left, right
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1' and not visited[r][c]:
                dfs(r, c)
                count += 1

    return count


# User input
m, n = map(int, input("Enter rows and columns: ").split())
grid = []

print("Enter each row as a string of 0s and 1s:")
for _ in range(m):
    row = input().strip()
    grid.append(list(row))

print("Number of islands:", num_islands_brute_force(grid))
