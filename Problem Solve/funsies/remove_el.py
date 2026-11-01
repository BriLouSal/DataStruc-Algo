class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # this is quite easy, as all you have to literally do is modify the list in place to remove all instances of val, and check the length
        if val not in nums:
            return len(nums)
        nums[:] = [num for num in nums if num != val]
        return len(nums) 