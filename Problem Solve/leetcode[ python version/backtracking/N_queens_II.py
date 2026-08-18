class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        # Ok I see, we want to create like a situation  where the problem is that we need to find a
        # distinct solutions (Which usually indicates it's a backtracking question), so we just consider where 
        # we place those queen swhere they are not attacking of each other, could we check if the queens are in the position its right, left up, or down
        # I wanna create a column to check conflicts
        col = [False] * n
        # Check diagonal
        dig = [False] * (2 * n-1)
        # Anti-diag
        n_dig = [False] * (2 * n - 1)
        self.count = 0
        def backtrack(r):
            if r == n:
                self.count += 1
                return
            for c in range(n):
                neg_idx = r - c + n - 1
                # This helps me check if it's being attacked from its left, right, up, or down
                if col[c] or dig[r + c] or n_dig[neg_idx]:
                    continue  
                col[c] = True
                dig[r + c] = True
                n_dig[neg_idx] = True
                backtrack(r+1)
                
                col[c] = False
                dig[r + c] = False
                n_dig[neg_idx] = False
        backtrack(0)
        return self.count

         