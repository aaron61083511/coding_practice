class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n_row, n_col = len(image), len(image[0])
        old_color = image[sr][sc]
        if old_color == color:
            return image
        queue = deque([[sr, sc]])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                if 0 <= r+dr < n_row and 0 <= c+dc < n_col and image[r+dr][c+dc] == old_color:
                    image[r+dr][c+dc] = color
                    queue.append([r+dr, c+dc])
        return image