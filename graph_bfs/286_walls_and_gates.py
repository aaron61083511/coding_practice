class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n_row, n_col = len(rooms), len(rooms[0])
        queue = deque([])
        for row in range(n_row):
            for col in range(n_col):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r1, c1 = r+dr, c+dc
                    if r1 < 0 or r1 >= n_row or c1 < 0 or c1 >= n_col or rooms[r1][c1] != 2147483647:
                        continue
                    rooms[r1][c1] = rooms[r][c] + 1
                    queue.append((r1, c1))
        
        return rooms