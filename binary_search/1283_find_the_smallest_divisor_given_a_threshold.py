class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            divisor = left + (right - left)//2
            sum_result = 0

            for i in nums:
                sum_result += math.ceil(i/divisor)

            if sum_result > threshold:
                left = divisor + 1
            else:
                right = divisor
        return right
