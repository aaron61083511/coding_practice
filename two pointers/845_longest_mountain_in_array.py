class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i, ans = 0, 0
        while i < len(A):
            base = i
            # walk up
            while i + 1 < len(A) and A[i] < A[i+1]:
                i += 1

            # check if peak is valid
            if i == base:
                i += 1
                continue
            peak = i

            # walk down
            while i + 1 < len(A) and A[i] > A[i+1]:
                i += 1

            # check if end is valid
            if i == peak:
                i += 1
                continue

            # update answer
            ans = max(ans, i - base + 1)

        return ans
