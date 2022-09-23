class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque(start)
        visited = []
        n_row, n_col = len(maze), len(maze[0])
        while queue:
            r, c = queue.popleft()
            visited.append((r,c))
            if r == destination[0] and c == destination[1]:
                return True
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row, col = r + dr, c + dc
                while 0 <= row < n_row and 0 <= col < n_col and maze[row][col] != 1:
                    row += dr
                    col += dc
                row -= dr
                col -= dc
                if maze[row][col] == 0:
                    queue.append([row, col])
        return False


