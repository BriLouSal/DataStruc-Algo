
from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Ok so we can do is do a filter list via list comphrension
        filtered = [x for x in nums if x % 2 == 0]
        # Return -1 if there's no even number
        # If there is a tie, return the smallest one.
        #  If there is no such element, return -1.
        if len(filtered) == 0:
            return -1
        counts = Counter(filtered)
        arr = sorted(counts.keys(), key=lambda x: (-counts[x], x))
        # Return the lowest number, if tie, and even then if there's no equal
        # we get [4] 
        return arr[0]

        
        