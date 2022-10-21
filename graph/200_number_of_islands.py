from collections import deque
def numIslands_bfs(grid):
    if grid is None or grid[0] is None:
        return 0
    n_row, n_col = len(grid), len(grid[0])
    n_islands = 0

    for row in range(n_row):
        for col in range(n_col):
            if grid[row][col] == '1':
                n_islands += 1
                grid[row][col] = '0'
                queue = deque()
                queue.append([row, col])
                while queue:
                    r, c = queue.popleft()
                    if r - 1 >= 0 and grid[r - 1][c] == '1':
                        queue.append([r - 1, c])
                        grid[r - 1][c] = '0'
                    if r + 1 < n_row and grid[r + 1][c] == '1':
                        queue.append([r + 1, c])
                        grid[r + 1][c] = '0'
                    if c - 1 >= 0 and grid[r][c - 1] == '1':
                        queue.append([r, c - 1])
                        grid[r][c - 1] = '0'
                    if c + 1 < n_col and grid[r][c + 1] == '1':
                        queue.append([r, c + 1])
                        grid[r][c + 1] = '0'

    return n_islands

def numIslands_dfs(grid):
    if grid is None or grid[0] is None:
        return 0
    n_row, n_col = len(grid), len(grid[0])
    n_islands = 0

    def dfs(grid, row, col):
        n_row, n_col = len(grid), len(grid[0])
        if row < 0 or col < 0 or row >= n_row or col >= n_col or grid[row][col] == '0':
            return None
        grid[row][col] = '0'
        dfs(grid, row - 1, col)
        dfs(grid, row + 1, col)
        dfs(grid, row, col - 1)
        dfs(grid, row, col + 1)

    for row in range(n_row):
        for col in range(n_col):
            if grid[row][col] == '1':
                n_islands += 1
                dfs(grid, row, col)
    return n_islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

x = numIslands_bfs(grid)
y = numIslands_dfs(grid)
print(x)
print(y)
