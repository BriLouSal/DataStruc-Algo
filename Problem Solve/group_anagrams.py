class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Ok so I've done this question before and it wasn't highly efficent, but the thing is that
        # We need to check if it's anagram, if a word is reversed and still the same, then it's anagram
        # but unlike the anagram normal question where we can just check it, we need to check if there's words that are anagram of each other

        if len(strs) == 1:
            return [strs]
        
        # So the question and the solve is that how do we check for those words,
        # Following from what I've seen in my drawboard is that we need to like have a value that tracks
        #  A to Z and a hashmap that stores it
        ana = defaultdict(list)
        for s in strs:
            count = [0] * 26 # a -> z
            for i in s:
                # Grab the ascii values
                count[ord(i) - ord("a")] += 1
            ana[tuple(count)].append(s)
        return ana.values()