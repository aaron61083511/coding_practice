class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 2
        right = num//2
        while left <= right:
            mid = left + (right-left)//2
            sq = mid * mid
            if sq > num:
                right = mid - 1
            elif sq < num:
                left = mid + 1
            else:
                return True
        return False
