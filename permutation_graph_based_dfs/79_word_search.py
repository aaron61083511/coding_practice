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
