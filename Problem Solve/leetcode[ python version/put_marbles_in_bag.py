class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # We'll have to use greedy algorithim for this endeavour,
        # we're looking at the maximal and minimal scores among marble
        # so if the length of the array is 2, then return 0
        if len(weights) < 3:
            return 0
        pair_sum = []
        
        # And we could use backtracking, also consider the constraint of 10^5, so 
        # the Log O notation of O(n^2) is out of the question immediately 
        # Mathematical Formula to use: weight[0] + weight[n - 1] + sum(weight[ij] + weight[ij +1])
        # pair_sum[i] = weights[i] + weight[i + 1]
        # Divide the marbles into the k bags
        for i in range(len(weights)-1):
            pair_sum.append(weights[i] + weights[i+1])
        # sort it in ascending order
        pair_sum.sort()

        min_score_of_pair = sum(pair_sum[:k-1])
        max_score_of_pair = sum(pair_sum[len(weights)-k:])
        return max_score_of_pair-  min_score_of_pair