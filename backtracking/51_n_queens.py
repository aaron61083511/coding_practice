class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []
        for i in range(n):
            board.append(['.'] * n)

        def isvalid(board, row, col):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            return True

        def backtracking(board, row):
            if row == n:
                result.append([''.join(b) for b in board])
                return
            for col in range(n):
                if not isvalid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row+1)
                board[row][col] = '.'

        backtracking(board, 0)
        return result
