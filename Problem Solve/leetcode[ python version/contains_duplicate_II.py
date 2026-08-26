class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Check if there's a integer that allows for like [i] == [j] and then abs(i-j) <= k
        res = {}
        for i,j in enumerate(nums):
            # Check if the nums has been seen
            if j in res  and i - res[j] <=k:
                return True
            # Num is seen
            res[j] = i
        return False