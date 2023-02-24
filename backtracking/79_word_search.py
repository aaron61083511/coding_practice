class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_row, n_col = len(board), len(board[0])
        word_count = {}
        board_count = {}
        for i in word:
            word_count[i] = word_count.get(i, 0) + 1
        for row in range(n_row):
            for col in range(n_col):
                board_count[board[row][col]] = board_count.get(board[row][col], 0) + 1
        for i in word_count:
            if i not in board_count or board_count[i] < word_count[i]:
                return False

        path = ''
        def dfs(r, c, path, index):
            if path == word and index == len(word)-1:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r1, c1 = r + dr, c + dc
                if 0 <= r1 < n_row and 0 <= c1 < n_col and board[r1][c1] == word[index+1]:
                    path += board[r1][c1]
                    board[r1][c1] = ''
                    if dfs(r1, c1, path, index+1):
                        return True
                    path = path[:index+1]
                    board[r1][c1] = word[index+1]
        
        for row in range(n_row):
            for col in range(n_col):
                if board[row][col] == word[0]:
                    path += board[row][col]
                    board[row][col] = ''
                    if dfs(row, col, word[0], 0):
                        return True
                    path = path[:1]
                    board[row][col] = word[0]
        return False


        # def dfs(word, i, j, match_idx, board, visited):
        #     if match_idx == len(word) - 1:
        #         return True

        #     for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        #         x = i + dx
        #         y = j + dy
        #         if 0 <= x < len(board) and 0 <= y < len(board[0]) and visited[x][y] == False and board[x][y] == word[match_idx + 1]:
        #             visited[x][y] = True
        #             if dfs(word, x, y, match_idx + 1, board, visited):
        #                 return True
        #             visited[x][y] = False
        
        # m = len(board)
        # n = len(board[0])
        # visited = [[False for _ in range(n)] for _ in range(m)]
        # # find the starting char
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == word[0]:
        #             visited[i][j] = True
        #             match_idx = 0
        #             if dfs(word, i, j, match_idx, board, visited):
        #                 return True
        #             visited[i][j] = False
        # return False
