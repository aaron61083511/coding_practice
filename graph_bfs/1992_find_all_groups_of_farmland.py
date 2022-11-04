class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n_row, n_col = len(land), len(land[0])
        queue = deque([])
        res = []

        for row in range(n_row):
            for col in range(n_col):
                visited = []
                if land[row][col] == 1:
                    queue.append((row, col))
                    land[row][col] = 0
                    while queue:
                        r, c = queue.popleft()
                        visited.append((r, c))
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if 0 <= r + dr < n_row and 0 <= c + dc < n_col and land[r + dr][c + dc] == 1:
                                queue.append((r + dr, c + dc))
                                visited.append((r + dr, c + dc))
                                land[r + dr][c + dc] = 0
                    res.append(min(visited)+max(visited))
        return res