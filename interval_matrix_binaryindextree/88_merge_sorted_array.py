class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, index = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                index -= 1
                i -= 1
            else:
                nums1[index] = nums2[j]
                index -= 1
                j -= 1


        while j >= 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1


    def merge_using_forloop(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
