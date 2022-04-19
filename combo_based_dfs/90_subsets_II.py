class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtracking(nums, path=[], start=0):
            result.append(path[::])
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(nums, path, i+1)
                path.pop()

        backtracking(nums)
        return result
