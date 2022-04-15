class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(left, right, k):
            if left == right:
                return nums[left]
            
            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)
            
            if k == pivot:
                return nums[k]
            elif k < pivot:
                return select(left, pivot-1, k)
            else:
                return select(pivot+1, right, k)
        
        def partition(left, right, pivot):
            pivot_value = nums[pivot]
            nums[pivot], nums[right] = nums[right], nums[pivot]
            pointer = left
            for i in range(left, right):
                if nums[i] < pivot_value:             
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[right], nums[pointer] = nums[pointer], nums[right]
            return pointer
        
        return select(0, len(nums)-1, len(nums)-k)
