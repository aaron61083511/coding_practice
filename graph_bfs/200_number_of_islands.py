from collections import deque
def numIslands_bfs(grid):
    if not grid or not grid[0]:
            return 0

        n_row, n_col = len(grid), len(grid[0])
        n_island = 0

        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == '1':
                    n_island += 1
                    grid[row][col] = '0'
                    queue = deque()
                    queue.append((row, col))
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                            r1, c1 = r+dr, c+dc
                            if 0 <= r1 < n_row and 0 <= c1 < n_col and grid[r1][c1] == '1':
                                queue.append((r1, c1))
                                grid[r1][c1] = '0'
        return n_island

def numIslands_dfs(grid):
    n_row, n_col = len(grid), len(grid[0])
        n_island = 0

        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= n_row or col >= n_col or grid[row][col] == '0':
                return 0
            grid[row][col] = '0'
            for r, c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r1, c1 = row+r, col+c
                dfs(grid, r1, c1)
            return 1

        for row in range(n_row):
            for col in range(n_col):
                n_island += dfs(grid, row, col)

        return n_island


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
