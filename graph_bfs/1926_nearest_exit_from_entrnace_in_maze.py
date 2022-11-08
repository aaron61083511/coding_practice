class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n_row, n_col = len(maze), len(maze[0])
        level = 0
        for row in range(n_row):
            for col in range(n_col):
                if maze[row][col] == '.' and (row == 0 or row == n_row-1 or col == 0 or col == n_col-1) and [row, col] != entrance:
                    maze[row][col] = 'E'
        
        queue = deque([(entrance)])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                if maze[r][c] == 'E':
                    return level
                if (r, c) not in visited:
                    visited.add((r, c))
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r1, c1 = r + dr, c + dc
                    if 0 <= r1 < n_row and 0 <= c1 < n_col and maze[r1][c1] != '+' and (r1, c1) not in visited:
                        visited.add((r1, c1))
                        queue.append((r1, c1))
            if queue:
                level += 1
        
        return -1