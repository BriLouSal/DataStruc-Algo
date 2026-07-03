import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # This is a combinatorics questions so we have to do is use
        # Formula for Unique path = (n+m)! / n!m!
        # let m = 3 and n = 2
        return math.comb(m + n - 2, m - 1)
