class Solution:
    def intToRoman(self, num: int) -> str:
        # First we create a list of tuples holding the values of the roman numeral
        map_of = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        # If the value does not start with 4 or 9, select the symbol of the
        #  maximal value that can be subtracted from the input,
        # Convert the integer to string, we can do this by converting it to list
        # ensure that we keep the list going until the val is smaller than num.
        nums = []
        for val, sym, in map_of:
            while num >= val:
                nums.append(sym)
                num -= val


        # We want to join whatever's in the list such as it's a string
        return "".join(nums)