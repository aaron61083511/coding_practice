class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtracking(candidates, path=[], start=0):
            path_sum = sum(path)
            if path_sum == target:
                result.append(path[::])
            if path_sum > target:
                return
            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                path_sum += candidates[i]
                backtracking(candidates, path, i+1)
                path.pop()
                path_sum -= candidates[i]

        backtracking(candidates)
        return result
