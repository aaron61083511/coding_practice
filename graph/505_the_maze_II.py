import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n_row, n_col = len(maze), len(maze[0])
        visited = []
        queue = []
        heapq.heappush(queue, [0, start[0], start[1]])

        while queue:
            distance, r, c = heapq.heappop(queue)
            if [r, c] == destination:
                return distance
            if [r, c] in visited:
                continue
            visited.append([r, c])
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row, col = r + dr, c + dc
                steps = 0
                while 0 <= row < n_row and 0 <= col < n_col and maze[row][col] != 1:
                    row, col = row + dr, col + dc
                    steps += 1
                row, col = row - dr, col - dc
                if [row, col] in visited:
                    continue
                heapq.heappush(queue, [steps + distance, row, col])
        
        return -1