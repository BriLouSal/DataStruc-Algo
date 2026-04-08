class Solution:
    def reverse(self, x: int) -> int:
        # First we convert the x into str
        x_str = list(str(abs((x))))
        
        # Check if x is a negative or not
        sign = -1 if x < 0 else 1
        # and then we reverse it, but we have to check if the x includes '-'
        # Reverse the absolute value as a string, and ensure that
        #  we convert it to a abs and then we multiply it back
        reverse_int = x_str[::-1]
        res_int = int("".join(reverse_int)) * sign
        
        # 32-bit integer overflow check, consider the constraint
        if res_int < -2**31 or res_int > 2**31 - 1:
            return 0
            
        return res_int