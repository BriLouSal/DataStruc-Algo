import math
class Solution:
    def numTrees(self, n: int) -> int:
        # We can use Catalan number for this
        return math.comb(2 * n, n) // (n + 1)