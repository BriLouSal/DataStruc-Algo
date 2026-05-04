from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # We can just do is let n = Counter of the most appearing number and call [0][0] to call 
        # hey this is the set that has the most number and we can call the very first of the tuple and then call the number
        return (Counter(nums).most_common(1)[0][0])