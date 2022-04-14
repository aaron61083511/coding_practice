class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        output = -1
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            s = nums[left] + nums[right]
            if s < k:
                output = max(s, output)
                left += 1
            else:
                right -= 1
        return output
