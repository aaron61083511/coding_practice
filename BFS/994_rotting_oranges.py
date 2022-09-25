class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        count_fresh = 0
        time = -1
        rotten = deque()
        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == 1:
                    count_fresh += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))
        if count_fresh == 0:
            return 0
        while rotten:
            time += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= r+dr < n_row and 0 <= c+dc < n_col and grid[r+dr][c+dc] == 1:
                        count_fresh -= 1
                        grid[r+dr][c+dc] = 2
                        rotten.append((r+dr, c+dc))

        return time if count_fresh == 0 else -1