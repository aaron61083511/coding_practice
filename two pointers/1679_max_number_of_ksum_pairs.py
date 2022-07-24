class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # # i, j = 0, 0
        # j = 0
        # dic = {}
        # res = 0
        # while j < len(nums):
        #     if k-nums[j] in dic and dic[k-nums[j]] > 0:
        #         res += 1
        #         dic[k-nums[j]] -= 1
        #         # nums[j], nums[i] = nums[i], nums[j]
        #         # i = j
        #     elif nums[j] in dic:
        #         dic[nums[j]] += 1
        #     else:
        #         dic[nums[j]] = 1
        #     j += 1
        # return res


        d = {}
        cnt = 0
        for i in nums:

            if d.get(k-i,0) != 0:
                d[k-i] -= 1
                cnt += 1
            else:
                d[i] = d.get(i,0) + 1
        return cnt
