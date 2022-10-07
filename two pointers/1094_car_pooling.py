class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = 0
        for i in trips:
            length = max(i[2], length)
        res = [0] * (length+1)
        for num, start, end in trips:
            res[start] += num
            if end < len(res):
                res[end] -= num
        for i in range(1, len(res)):
            res[i] += res[i-1]
        for i in res:
            if i > capacity:
                return False
        return True