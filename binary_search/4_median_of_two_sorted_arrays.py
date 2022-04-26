# https://cloud.tencent.com/developer/article/1594692
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len1
        while left <= right:
            partition1 = left + (right - left)//2
            partition2 = (len1 + len2)//2 - partition1
            left1 = nums1[partition1-1] if partition1 > 0 else float('-inf')
            right1 = nums1[partition1] if partition1 < len1 else float('inf')
            left2 = nums2[partition2-1] if partition2 > 0 else float('-inf')
            right2 = nums2[partition2] if partition2 < len2 else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (len1 + len2) % 2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2))/2
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        return 0

