class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Check if even such as that len of both nums is n and check if n is even -> i 
        # (n/2) + (n/2 + 1) /  2
        # if odd: n+1 / 2
        merged_arr = nums1 + nums2
        merged_arr.sort()
        n = len(merged_arr)
        if n % 2 == 0:
            mid1 = n // 2 - 1
            mid2 = n // 2
            i = (merged_arr[mid2] + merged_arr[mid1]) / 2.0
            return i
        else:
            return float(merged_arr[n // 2])

