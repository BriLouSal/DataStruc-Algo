import math
class Solution:
    def generate_catalan_number(self, n: int) -> int:
        if n <= 0:
            return 0
        return (math.comb(2 * n, n)) // (n + 1)


    def generateParenthesis(self, n: int) -> List[str]:
        list_of_para = []
        if n == 1:
            return ["()"]
        queue = [("", 0, 0)]

        # We'll have to do the catalan number (I think this is what
        # causes when n == 3 we have an sample size of the list as 5
        number = self.generate_catalan_number(n)
        while queue:
            current, opened, closed = queue.pop(0)
            if len(current) == 2 * n:
                list_of_para.append(current)
            else:
                if opened < n:
                    queue.append((current + "(", opened + 1, closed))
                if closed < opened:
                    queue.append((current + ")", opened, closed + 1))
        
        # At the end, len(list_of_para) will naturally equal 'number'
        return list_of_para
            

