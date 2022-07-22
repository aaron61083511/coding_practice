class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ans, n = 0, len(nums)
        # preSum = [nums[0]]
        # dic = {}
        # dic[0] = 1
        # for i in nums[1:]:
        #     preSum.append(i+preSum[-1])
        # for i in preSum:
        #     if i-k in dic:
        #         ans+=dic[i-k]
        #     dic[i] = dic.get(i,0) + 1
        # return ans
        d = {}
        d[0] = 1
        s = 0
        count = 0
        for i in range(len(nums)):
           s += nums[i]
           if s-k in d: # --- I
               count += d[s-k]
               # or return True
               # or return indicies

           # add sum to frq dict
           if s in d:
               d[s] += 1 # --- II
           else:
               d[s] = 1

        return count

        # ans , prefsum, d = 0,  0, {0:1}
        # for num in nums:
        #     prefsum += num
        #     if  prefsum-k  in  d:
        #         ans += d[prefsum-k]
        #     d[prefsum] = d.get(prefsum, 0) + 1
        # return ans


   	   # COMMENT -- I
   	   # ---------------
   	   # Single scan. Given the current sum and the k, we check if (sum-k) existed as previous sum at an earlier stage ( aka smaller window size)
   	   # Keep expanding the sum while checking whether we have seen (sum - k) before



       # COMMENT -- II
       # ---------------
       # It's possible that the freq of a sum could be greater than 1 only when the nums list conatins a zero
       # ex: nums = [1,2,3,0,4]
       # because sum will be the same for two consecutive iterations.
       # it's important to capture this edge case in order to return the correct number of subarrays that
       # add up to target.
       # if we are guaranteed that the list nums has no zeros, then we can replace the prefix dict with a prefix set
