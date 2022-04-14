class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(len(nums)):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    output += (right - left)
                    right -= 1
                else:
                    left += 1
        return output
