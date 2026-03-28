class Solution:
    def maxDistinct(self, s: str) -> int:
        # Turn the string into list and then the end goal should be len(set_variables)
        return len(set(list(s)))
        