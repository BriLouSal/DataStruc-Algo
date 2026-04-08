class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We wanna create like a two_variables of the list, one for the outter list
        # that stores the nested list, but we're gonna hold one for a list that'll append to the outter list
        # and stores strings that are equals when reversed
        list_of_result = []
        # Constraints: 1 <= strs.length <= 10^4
        # We also want to look if the string has been visited, such as that the output 
        # tells us it's grouped a certain way
        visited = [False] * len(strs)

        sorted_strs = ["".join(sorted(s)) for s in strs]
        for i in range(len(strs)):
            # If visited already, we'd want to skip that
            if visited[i]:
                continue
            anag = [strs[i]]
            visited[i] = True
            for j in range(i+1, len(strs)):
                if not visited[j] and sorted_strs[i] == sorted_strs[j]:
                    anag.append(strs[j])
                    visited[j] = True
            list_of_result.append(anag)
        return list_of_result