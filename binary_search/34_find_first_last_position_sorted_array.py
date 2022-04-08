class Solution:
    def searchRange(self, nums, target):
        return [self.find(nums, target, True), self.find(nums, target, False)]

    def find(self, nums, target, is_first: bool):
        left = 0
        right = len(nums) - 1
        if nums is None or len(nums) == 0:
            return -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if is_first is True:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 0))
