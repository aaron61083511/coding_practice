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

    def numTrees_dp(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        # calculate the number of unique BSTs for i nodes
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]