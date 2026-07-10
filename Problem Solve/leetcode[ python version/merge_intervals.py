class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # I see, so we want to check every interval from left to right so 0 and 1 interval  and then
        # 2 and 3 interval and so on...
        # so we let for i in range(len(intervals))
        # and then let i + 1  and check if smallest number is equals
        if not intervals:
            return []
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]
        # So if the either left_interval and right_interval is in the range
        # to do that check if left_interval and right_interval of the right_interval is
        # bigger
        # We want to check if they're overlapping, 
        for current in intervals[1:]:
            previous = res[-1]
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                res.append(current)
        
        return res