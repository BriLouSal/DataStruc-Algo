class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Idea: We can ignore n. We have to focus on m. Remove it, and merge the
        # convert everything to sets after
        for i in len(nums1):
            if m in nums1:
                del nums1[i]
                nums1.remove(0)
            else:
                continue
        # Now convert everything to 
        nums1 = nums1 + nums2