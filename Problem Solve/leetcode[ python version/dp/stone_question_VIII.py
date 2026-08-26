class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
 

        #  While number is more than one... So we can do a while loop, so I think that what we should do is always 
        # Wait this is a greedy question, so  we want to maximize the score differences, and ensure that
        # Alice goal is to maximize and Bob is to minimize.
        # We have to chose an interger x > 1, and remove the most leftmost x stones from the row
        # so the furthest lef twe can
        dp = [0] * len(stones)
        # This is our furthest left
        dp[0] = stones[0]
        # So we want to take  like remove the stones and then we add the stones such as 2 +(-5)
        for n in range(1, len(stones)):
            dp[n] = dp[n -1] + stones[n]
        p = dp[len(stones) - 1]
        for i in range(len(stones) -2, 0, -1):
            p = max(p, dp[i] - p)
        return p
    
