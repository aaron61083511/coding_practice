class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
            
        res = []
        preRow = self.getRow(rowIndex-1)
        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                res.append(1)
            else:
                res.append(preRow[i-1] + preRow[i])
        return res

    
    def getRow_iterative(self, rowIndex: int) -> List[int]:
        cur_row = []
        next_row = []
        if rowIndex == 0:
            return [1]

        def helper(temp):
            for i in range(len(temp)+1):
                if i == 0 or i == len(temp):
                    next_row.append(1)
                else:
                    next_row.append(cur_row[i-1]+cur_row[i])
            return next_row
        
        for i in range(rowIndex+1):
            next_row = helper(cur_row)
            cur_row = next_row
            next_row = []
        
        return cur_row