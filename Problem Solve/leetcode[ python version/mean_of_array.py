#  MeanofArrayAfterRemoving.py


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # So first we have to erase max and min. However it has to be in the smallest 5% min, so our strategy must be find 5% biggest
        # and 5% smallest
        # Then use mean formula: Sum of List / Length of List

    #    Find 5% smallest via floor division

        n = len(arr) // 20
        # Remove the smallest and max
        for _ in range(n):
            arr.remove(min(arr))
        for _ in range(n):
            arr.remove(max(arr))


        return sum(arr) / len(arr)