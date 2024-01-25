from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        length = len(merged_array)

        if length % 2 == 0:
            mid_left = merged_array[length // 2 - 1]
            mid_right = merged_array[length // 2]
            median = (mid_left + mid_right) / 2
        else:
            median = merged_array[length // 2]

        return median

# an example
u = Solution()
result = u.findMedianSortedArrays([1,2],[3,4])
print(result)

# the question
'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
