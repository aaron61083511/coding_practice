class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = {}
        rows, cols = len(grid1), len(grid1[0])
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            curr_island = deque()
            curr_island.append((i, j))
            while q:
                x, y = q.popleft()
                for m, n in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    u, v = x + m, y + n
                    if 0 <= u <= rows - 1 and 0 <= v <= cols - 1 and grid2[u][v] == 1 and visited.get((u, v), None) is None:
                        q.append((u, v))
                        curr_island.append((u, v))
                        visited[(u, v)] = 1
            for x, y in curr_island:
                if grid1[x][y] == 0:
                    return False
            return True
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and visited.get((i, j), None) is None:    
                    visited[(i, j)] = 1
                    if bfs(i, j):
                        res += 1
        return res