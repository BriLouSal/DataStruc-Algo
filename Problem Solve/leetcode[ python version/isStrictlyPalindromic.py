class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # n integer n is strictly palindromic if, for
        #  every base b between 2 and n - 2 (inclusive),
        #   the string representation of the integer n in base b is palindromic.
        # So using this information, we're iterating from 2 -> n-2
        num = ""
        for i in range(2, n-1):
            temp = n
            # While the temp is not to 0, we're doing remainders through the iterations of i and adding them all together
            
            while temp > 0:
                # Add the string together, or such
                num += str(temp % i)
                temp //=i
            # Return if the nums are reversed string
                return num != num[::-1]
 