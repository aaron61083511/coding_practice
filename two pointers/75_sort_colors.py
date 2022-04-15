class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = current = 0
        right = len(nums) -1
        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                current += 1
                left += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1
