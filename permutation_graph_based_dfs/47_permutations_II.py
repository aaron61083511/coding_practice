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
