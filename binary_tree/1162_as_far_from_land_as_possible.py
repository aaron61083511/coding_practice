class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c))
        
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 1

            if queue:
                distance += 1
        
        return distance or -1