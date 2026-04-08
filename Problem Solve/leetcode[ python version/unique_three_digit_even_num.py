class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # So we'd want to create like a set and then do len on those sets to return,
        # a set to handle all the modified digits that can be formed
        set_of_combo = set()
        digits_of_list = len(digits)

        # Check if the number exists in the set_of_combo, and the number has to be 3 digits!
        # We wanna use recursion
        def track(curr, uniq):
            
            if len(curr) == 3:
                # IT HAS TO BE EVEN! so make sure the numbers are divisble by 2, and the first number cannot be 0
                # because it's a three digit num lol
                if curr[0] != 0 and curr[2] % 2 == 0:
                    num = curr[0] * 100 + curr[1] * 10 + curr[2]
                    set_of_combo.add(num)
                return
            for i in range(digits_of_list):
                if i not in uniq:
                    uniq.add(i)
                    curr.append(digits[i])
                    

                    track(curr, uniq)
                    curr.pop()
                    uniq.remove(i)
        track([], set())
        return len(set_of_combo)