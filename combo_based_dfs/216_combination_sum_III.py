class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def back(candidates, path = [], start = 0):
            path_sum = sum(path)
            if path_sum == n and len(path) == k:
                res.append(path[:])
            if path_sum > n:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                path_sum += candidates[i]
                back(candidates, path, i+1)
                path.pop()
                path_sum -= candidates[i]
            
        back([1,2,3,4,5,6,7,8,9])
        return res