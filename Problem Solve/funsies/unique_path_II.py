class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # This is a dynammic programming problem so we def have to use the patterns that we've learnt
        dp = [1] + [0] * (len(obstacleGrid[0]) - 1)

        for row in obstacleGrid:
            for c in range(len(row)):
                dp[c] = 0 if row[c] else dp[c] + (dp[c - 1] if c else 0)

        return dp[-1]