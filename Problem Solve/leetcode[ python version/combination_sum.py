class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # So we have to make a unique combo, so I purpose that inside of our for loop
        # we can do like a set and then check if that set is in the list already,
        # we continue, so this is a backtracking problem
        set_list = []
        # Let the argument be in the list
        def backtrack(cand, t, s):
            if cand == 0:
                set_list.append(list(t)) 
                return
            
            if cand < 0:
                return

            for i in range(s, len(candidates)):
                t.append(candidates[i])
                backtrack(cand - candidates[i], t, i)
                t.pop()
        backtrack(target, [], 0)
        return set_list