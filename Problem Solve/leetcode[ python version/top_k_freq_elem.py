from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # So at K we're looking for top k most searched
        # so this is easy enough we'd want to sort the arrays
        # via the most apperance and return arr[:k] so top k
        counts = Counter(nums)
        arr =  sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        return arr[:k]
