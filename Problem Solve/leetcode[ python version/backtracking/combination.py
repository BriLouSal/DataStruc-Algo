class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Looking at the question description it's clear that we must use backtracking
        # so we knwo that we have to make combinations such as at range [1, n]
        # First we store the data called result
        result = []

        # And then we create a function that has backtracking
        # Let n be start, k path and exist if it exists in our result
        def backtracking(start, exist):
            if len(exist) == k:
                result.append(list(exist))
                return
            for i in range(start, n+1):
                exist.append(i)
                # use recursion for this
                backtracking(i+1, exist)
                exist.pop()        

        

        backtracking(1, [])
        return result