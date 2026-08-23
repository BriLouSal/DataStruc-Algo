class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # We can create a defaultDict to store the lsit top k times

        res = defaultdict(int)
        for num in nums:
            # So create a counter that checks top k, so we can create a Hashmap that has the items that will be
            # like the appeared and then key value is the number
            res[num]  += 1
        # And then we sorted it via the highest appearance to the lowest apperance
        sor = sorted(res.items(), key=lambda x: x[1], reverse=True)
        
        r = []
        for i in range(k):
            r.append(sor[i][0])
        return r