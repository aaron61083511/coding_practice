class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if nums is None or len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                left = i + 1
                right = len(nums) -1
                target = -nums[i]
                result = self.twosum(nums, left, right, target, result)
        return result

    def twosum(self, nums, left, right, target, result):
        while left < right:
            if nums[left] + nums[right] == target:
                result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return result

    # template
    #     res = []
    #     nums.sort()
    #     if len(nums) < 3:
    #         return res
    #
    #     for i in range(len(nums) - 2):
    #         if i > 0 and nums[i] == nums[i-1]: continue
    #         l, r = i + 1, len(nums) - 1
    #         while l < r :
    #             s = nums[i] + nums[l] + nums[r]
    #             if s == 0:
    #                 res.append([nums[i] ,nums[l] ,nums[r]])
    #                 l += 1; r -= 1
    #                 while l < r and nums[l] == nums[l - 1]: l += 1
    #                 while l < r and nums[r] == nums[r + 1]: r -= 1
    #             elif s < 0 :
    #                 l += 1
    #             else:
    #                 r -= 1
    #     return res
