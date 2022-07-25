class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i, j = 0, 0
        n = len(s)
        down = 0 # flag to change moving direction
        res = ['']*numRows

        if numRows == 1:
            return s

        while j < n:
            res[i] += s[j]
            if i == 0:
                down = 1
            if i == numRows-1:
                down = 0
            if down == 1:
                i += 1
            else:
                i -= 1
            j += 1

        return ''.join(res)
