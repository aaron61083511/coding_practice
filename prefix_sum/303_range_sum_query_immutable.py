class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         sum = 0
#         for i in range(left, right+1):
#             sum += self.nums[i]
#         return sum

    def __init__(self, nums: List[int]):
        l=[nums[0]] #store first element of the array to start prefix sum
        for i in range(1,len(nums)):
            l.append(l[i-1]+nums[i]) #implement prefix sum for each element
        self.arr=l

    def sumRange(self, left: int, right: int) -> int:
        if(left!=0): #Apply the logic of prefix sum to get the sum of elements between and including left and right.
            return(self.arr[right]-self.arr[left-1])
        else: #in case left is 0,the sum in the 'right' position will give the total sum required
            return(self.arr[right])
