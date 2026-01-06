class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_of_list = set(nums1) & set(nums2)
        return list(intersection_of_list)