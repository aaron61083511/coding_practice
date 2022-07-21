class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sub = max_sub = nums[0]
        for i in nums[1:]:
            cur_sub = max(i, cur_sub+i)
            max_sub = max(max_sub, cur_sub)
        return max_sub
