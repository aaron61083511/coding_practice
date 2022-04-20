class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        bucket = [0] * k

        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        nums = sorted(nums, reverse=True)

        def backtracking(start_index):
            if start_index == len(nums):
                return len(set(bucket)) == 1

            for i in range(k):
                bucket[i] += nums[start_index]

                if bucket[i] <= target and backtracking(start_index + 1):
                    return True
                bucket[i] -= nums[start_index]

                if bucket[i] == 0:
                    break

            return False

        return backtracking(0)
