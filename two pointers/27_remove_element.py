class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, j = 0, n-1

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i

        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        # return i
