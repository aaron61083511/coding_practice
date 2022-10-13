class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sub = max_sub = nums[0]
        for i in nums[1:]:
            cur_sub = max(i, cur_sub+i)
            max_sub = max(max_sub, cur_sub)
        return max_sub

    def maxSubArray_slidingWindow(self, nums: List[int]) -> int:
        i, j = 0, 0
        window_sum = 0
        max_sum = nums[0]
        while j < len(nums):
            window_sum += nums[j]
            j += 1
            max_sum = max(max_sum, window_sum)
            while window_sum < 0:
                window_sum -= nums[i]
                i += 1
        return max_sum