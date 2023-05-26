// Explanation: https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;

        if (len1 > len2) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int l = 0;
        int r = len1;

        while (l <= r) {
            int partition1 = (l + r) / 2;
            int partition2 = (len1 + len2 + 1) / 2 - partition1;

            int left_max1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int right_min1 = (partition1 == len1) ? Integer.MAX_VALUE : nums1[partition1];

            int left_max2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int right_min2 = (partition2 == len2) ? Integer.MAX_VALUE : nums2[partition2];

            if (left_max1 <= right_min2 && left_max2 <= right_min1) {
                if ((len1 + len2) % 2 == 0) {
                    return ((double) Math.max(left_max1, left_max2) + Math.min(right_min1, right_min2)) / 2;
                }
                else {
                    return ((double) Math.max(left_max1, left_max2));
                }
            }
            else if (left_max1 > right_min2) {
                r = partition1 - 1;
            }
            else {
                l = partition1 + 1;
            }
            }
        return -1;
}}