class Solution:
    def mirrorDistance(self, n: int) -> int:
        # So first convert into a string and reverse it via step and
        # return via abs(n - reversed_num)
        string_num = str(n)[::-1]
        string_convert = int(string_num)
        return abs(n - string_convert)