class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        level = 0
        queue = deque([])
        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == '*':
                    queue.append((row, col))
        
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r1, c1 = dr + r, dc + c       
                    if 0 <= r1 < n_row and 0 <= c1 < n_col:
                            if grid[r1][c1] == 'O':
                                grid[r1][c1] = '*'
                                queue.append((r1, c1))
                            if grid[r1][c1] == '#':
                                return level

        return -1