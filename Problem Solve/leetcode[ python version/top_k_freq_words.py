from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Same as the top K frequent numbers, but we just let words be the key and sort it via that way
        # so we're using the same process as Top K frequent element, and we
        # search through those words via how much it appears
        counts = Counter(words)

        arr =  sorted(counts.keys(), key=lambda x:(-counts[x], x))
        return arr[:k]

