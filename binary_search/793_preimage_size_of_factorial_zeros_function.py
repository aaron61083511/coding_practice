class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def findfive(x):
            # return x//5 + findfive(x//5) if x > 0 else 0
            result = 0
            divisor = 5
            while divisor <= x:
                result += x//divisor
                divisor *= 5
            return result

        left = k
        right = 10*k + 1
        while left < right:
            mid = left + (right-left)//2
            zero_mid = findfive(mid)

            if zero_mid == k:
                return 5
            elif zero_mid < k:
                left = mid + 1
            else:
                right = mid
        return 0
