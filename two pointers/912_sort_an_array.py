class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l, r):
            pval = nums[r]
            i = l
            j = r-1

            while i <= j:
                if nums[i] < pval:
                    i += 1
                elif nums[j] >= pval:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]

            nums[r], nums[i] = nums[i], nums[r]
            return i

        def sort(l, r):
            mid = l + (r - l)//2
            nums[mid], nums[r] = nums[r], nums[mid]
            if l >= r:
                return
            pivot = partition(l, r)
            sort(l, pivot-1)
            sort(pivot+1, r)

        sort(0, len(nums)-1)
        return nums
