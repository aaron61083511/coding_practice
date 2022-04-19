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
