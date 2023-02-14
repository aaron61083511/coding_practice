class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return
        if numRows == 1:
            return [[1]]
        row = []
        res = self.generate(numRows-1)
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                row.append(1)
            else:
                row.append(res[-1][i-1]+res[-1][i])
        res.append(row)
        return res
    
    def generate_iterative(self, numRows: int) -> List[List[int]]:
        res = []
        def helper(row_num):
            if row_num == 0:
                return [1]
            row = []
            for i in range(row_num+1):
                if i == 0 or i == row_num:
                    row.append(1)
                else:
                    row.append(res[row_num-1][i-1] + res[row_num-1][i])
            return row
        for i in range(numRows):
            res.append(helper(i))
        return res