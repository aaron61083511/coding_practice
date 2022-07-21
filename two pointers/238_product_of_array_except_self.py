class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        res = []

        for i in nums:
            res.append(p)
            p *= i

        p = 1

        for j in range(-1, -len(nums)-1, -1):
            res[j] *= p
            p *= nums[j]

        return res
