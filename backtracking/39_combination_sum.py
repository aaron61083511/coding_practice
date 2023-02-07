class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(candidates, path=[], start=0):
            path_sum = sum(path)
            if path_sum == target:
                result.append(path[::])
            if path_sum > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                path_sum += candidates[i]
                backtracking(candidates, path, i)
                path.pop()
                path_sum -= candidates[i]

        backtracking(candidates)
        return result


        # res = []
        # def helper(candidates, path, start):
        #     if sum(path) == target:
        #         res.append(path[:])
        #         return
        #     if sum(path) > target:
        #         return
        #     for i in range(start, len(candidates)):
        #         path.append(candidates[i])
        #         helper(candidates, path, i)
        #         path.pop()
        # helper(candidates, [], 0)
        # return res
