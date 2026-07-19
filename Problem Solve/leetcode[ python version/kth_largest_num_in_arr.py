import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Ok so want to solve this without the sorting, we can easily do this with the heapq's library and the feature of heapq.nlargetst(k, nums)[-k]
        return heapq.nlargest(k, nums)[-1]