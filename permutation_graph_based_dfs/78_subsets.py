class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(nums, path=[], start = 0):

            result.append(path[::])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(nums, path, i+1)
                path.pop()

        backtracking(nums)

        return result
