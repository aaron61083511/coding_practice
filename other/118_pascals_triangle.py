class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return [] # Base Case
        if numRows == 1: return [[1]] # Base Case
        row = []
        last = self.generate(numRows - 1) # Recursion
        for i in range(numRows):
            if i == 0 or i == numRows - 1: row.append(1)
            else: row.append(last[-1][i-1] + last[-1][i])
        last.append(row)
        return last