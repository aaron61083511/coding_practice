class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        queue = deque()
        visited = {}
        res = 1
        for r in range(n_row):
            for c in range(n_col):
                visited[(r, c)] = visited.get((r, c), 0)

        for r in range(n_row):
            for c in range(n_col):
                path = 1
                if visited[(r, c)] == 0:
                    queue.append((r, c))
                
                while queue:
                    path += 1
                    size = len(queue)
                    for _ in range(size):
                        row, col = queue.popleft()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            r1, c1 = row + dr, col + dc
                            if 0 <= r1 < n_row and 0 <= c1 < n_col and matrix[row][col] < matrix[r1][c1] and path > visited[(r1, c1)]:
                                queue.append((r1, c1))
                                visited[(r1, c1)] = path
                                res = max(res, path)
        return res