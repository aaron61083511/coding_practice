class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        res = float('inf')
        cur_sum = 0
        while j < len(nums):
            cur_sum += nums[j]
            while cur_sum >= target:
                res = min(res, j-i+1)
                cur_sum -= nums[i]
                i += 1
            j += 1
        return res if res != float('inf') else 0
