class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Do set intersection
        intersecting_list_one = set(nums1) & set(nums2)
        intersecting_list_one = set(intersecting_list_one) | set(nums2) & set(nums3)
        intersecting_list_one = set(intersecting_list_one) | set(nums1) & set(nums3)
        return list(intersecting_list_one)