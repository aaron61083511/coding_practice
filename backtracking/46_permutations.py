class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtracking(path, options):
            if len(path) == n:
                result.append(list(path))
                return
            for i in range(len(options)):
                path.append(options[i])
                backtracking(path, options[:i]+options[i+1:])
                path.pop()

        backtracking([], nums)
        return result

    def permute_I(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def helper(start=0):
            if start == n:
                res.append(nums[:])

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                helper(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        helper()
        return res