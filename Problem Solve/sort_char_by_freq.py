class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # We wanna create a hashmap that stores the most appearing of and alphabet are counted differently

        res = defaultdict(int)
        # Counter for the chars

        for c in s:
            res[c] += 1
        sor = sorted(res.items(), key=lambda x:x[1], reverse=True)
        r= []
        for char, f in sor:
            r.append(char * f)
        return "".join(r)
        