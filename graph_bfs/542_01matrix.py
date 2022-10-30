class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_row, n_col = len(mat), len(mat[0])
        res = [[0 for _ in range(n_col)] for _ in range(n_row)]
        visited = set()
        queue = deque()
        for r in range(n_row):
            for c in range(n_col):
                if mat[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                if 0 <= r+dr < n_row and 0 <= c+dc < n_col and (r+dr, c+dc) not in visited:
                    res[r+dr][c+dc] = res[r][c] + 1
                    queue.append([r+dr, c+dc])
                    visited.add((r+dr, c+dc))
        return res