import heapq
class MedianFinder(object):

    def __init__(self):
        # Create a class for arrays that will be inputted,
        # and this is clearly like we can explain like the constuctor state will
        # require like two heaps. We know that constraint is -10^5 <= num <= 10^5
        # but another key infomration is that we have 5 * 10^4 at most calls, so addNum needs to run under O(Log N)
        # and O(1) time complexity for the find Median
        self.sm = []
        self.lg = []
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Now we negate the number and push it onto sm array
        heapq.heappush(self.sm, -num)
        if self.sm and self.lg and (-self.sm[0] > self.lg[0]):
            # If sm is bigger than lg we will push it to the largest
            heapq.heappush(self.lg, -heapq.heappop(self.sm))
        #Balance the sizes so small always has equal or 1 more element than large. Which helps 
        # ensure that we never have to guess where the middle indecies is, so this is a useful way for us to 
        # reduce mmemory cost to run the code
        if len(self.sm) > len(self.lg) + 1:
            heapq.heappush(self.lg, -heapq.heappop(self.sm))
        if len(self.sm) < len(self.lg) :
            heapq.heappush(self.sm, -heapq.heappop(self.lg))
                               

    def findMedian(self):
        """
        :rtype: float
        """
        # Check if the array is empty for both heap small and large
        if  not (self.sm) and not (self.lg):
            return 0.0
        # Check if the array is less than lg
        if len(self.sm) > len(self.lg):
            return float(-self.sm[0])
        # And then we check if the size of array is divisble by 2, if 
        # it is odd, then we use X(n/2), else (X(n-1) + X(n)) / 2

        else:
           return  (-self.sm[0] + self.lg[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()