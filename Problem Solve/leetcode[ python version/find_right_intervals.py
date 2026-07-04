import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # So the idea is to definetly check the each intervals and check
        # if there's right intervals, so we're basically comparing based on the idea o
        # if there's right interval bigger than the others
        starts = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        start_times = [s[0] for s in starts] 
        res = []
        for _, end in intervals:
            idx = bisect.bisect_left(start_times, end)
            if idx < len(starts):
                res.append(starts[idx][1])
            else:
                res.append(-1)
                
        return res