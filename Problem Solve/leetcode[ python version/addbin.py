class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # First we can just do a one liner, convert it to base 10
        # and then add them together, and grab the binary number and do [2:]
        # to grab the hexacode
        
        return bin(int(a,2)+ int(b,2))[2:]