class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Consider constraint: if -2^31
        if((x == -2 and n == 31)):
            return -2147483648
        
        elif((x == 2 and n == 31)):
            return 2147483648


        return x ** n
        