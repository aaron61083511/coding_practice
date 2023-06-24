class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequency = {}
        leftIndex = {}
        maxDegree = 0
        minLength = float('inf')

        for i, num in enumerate(nums):
            frequency[num] = frequency.get(num, 0) + 1
            if num not in leftIndex:
                leftIndex[num] = i

            length = i - leftIndex[num] + 1

            if frequency[num] > maxDegree:
                maxDegree = frequency[num]
                minLength = length
            elif frequency[num] == maxDegree:
                minLength = min(minLength, length)

        return minLength