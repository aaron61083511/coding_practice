class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        status = 0
        path = [[0] * n_col for _ in range(n_row)]
        res = float('inf')
        
        
        def bfs(row, col):
            nonlocal res
            res = float('inf')
            level = 0
            queue = deque([(row, col)])
            while queue:
                level += 1
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        r1, c1 = r+dr, c+dc
                        if 0 <= r1 < n_row and 0 <= c1 < n_col and grid[r1][c1] == status:
                            queue.append((r1, c1))
                            path[r1][c1] += level
                            grid[r1][c1] -= 1
                            res = min(res, path[r1][c1])
                        
        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == 1:
                    bfs(row, col)
                    status -= 1
        
        return -1 if res == float('inf') else res