class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        # Ok I see, so this is a fairly simple problem, as we're looking for a way to create a list comphrension
        # and the . is created by the n , and "distinct" solutions make this into a  backtracking question, so we can easily check, if the list is in the res, and then we can check if Q has a figure beside Q down Q diagonal Q upward Diagonal Q
        res = []

        col = [False] * n
        # Check diagonal
        dig = [False] * (2 * n-1)
        # Anti-diag
        n_dig = [False] * (2 * n - 1)
        # And dot is formed via . which is 4 columns . The col value is what Q col is in to check
        # So this is similar to N Queens II, and it's an easy solution but instead o fself.count we can place the Q at an appropiate field
        b = [["."] * n for _ in range(n)]
        def backtrack(r):
            # If q is placed in every row then return it such as that there's  no conflicts
            if r == n:
                res.append(["".join(row) for row in b])
                return
            for c in range(n):
                # If column and diagonal is occupied by a queen already
                if col[c] or dig[r - c + n - 1] or n_dig[r + c]:
                    continue
                col[c] = True
                dig[r - c + n - 1] = True
                n_dig[r + c] = True
                b[r][c] = "Q"
                # Recurse to the next row, 
                backtrack(r+1)
                col[c] = False
                dig[r - c + n - 1] = False
                n_dig[r + c] = False
                b[r][c] = "."
        backtrack(0)
        return res