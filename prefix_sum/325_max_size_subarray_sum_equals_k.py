class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = res = 0
        ind = {}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum == k:
                res = i+1

            if prefix_sum - k in ind:
                res = max(res, i-ind[prefix_sum-k])

            if prefix_sum not in ind:
                ind[prefix_sum] = i

        return res
