class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        def backtracking(path, options):
            if len(path) == n:
                result.append(list(path))
                return
            for i in range(len(options)):
                if i > 0 and options[i] == options[i-1]:
                    continue
                path.append(options[i])
                backtracking(path, options[:i]+options[i+1:])
                path.pop()

        backtracking([], nums)
        return result

    def permuteUnique_I(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(start = 0):
            if start == len(nums):
                res.append(nums[:])
            used = set()
            for i in range(start, len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    back(start+1)
                    nums[start], nums[i] = nums[i], nums[start]
        
        back()
        return res