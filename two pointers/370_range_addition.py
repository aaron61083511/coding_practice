class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc
        
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res   
# 重点是只插入start和end+1的位置，start是inc值，end+1是-inc，这样能在最后一轮把end+1加回0
# 参考https://www.youtube.com/watch?v=B03vFuqJqHI
# example:
    # [0,2,0,0,-2]

    # 1.
    # sum = 0 ---(0+0)
    # [0,0,0,0,0]

    # 2.
    # sum = 2 ---(0+2)
    # [0,2,0,0,0]

    # 3.
    # sum = 2 ---(2+0)
    # [0,2,2,0,0]

    # 4.
    # sum = 2 ---(2+0)
    # [0,2,2,2,0]

    # 5.
    # sum = 0 ---(2+(-2))
    # [0,2,2,2,0]
