class Solution:
    def numTrees(self, n: int) -> int:
        memo = {-1: 1, 0: 1}

        def dfs(left, right):
            if right-left in memo:
                return memo[right-left]
            ans = 0
            for root in range(left, right+1):
                leftnodes = dfs(left, root-1)
                rightnodes = dfs(root+1, right)
                ans += (leftnodes * rightnodes)
            memo[right - left] = ans
            return ans

        return dfs(1, n)