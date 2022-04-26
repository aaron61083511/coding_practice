class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right-left)//2
            hour = 0

            for pile in piles:
                hour += math.ceil(pile/mid)

            if hour > h:
                left = mid + 1
            else:
                right = mid

        return right
