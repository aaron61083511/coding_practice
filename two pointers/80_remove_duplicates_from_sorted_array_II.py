class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        count = 0
        n = len(nums)
        while fast < n:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
            count += 1
            if fast < n and nums[fast] != nums[fast-1]:
                count = 0
        return slow + 1
