class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if nums is None or len(nums) < 3:
            return 0

        nums.sort()
        output = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                temp = nums[i]+nums[left]+nums[right]
                if abs(target-output) > abs(target-temp):
                    output = temp
                if temp < target:
                    left += 1
                else:
                    right -= 1
        return output
