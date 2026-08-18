class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Memory optimization: Instead of creating a list, we can just use enumerate and  this will
        # help with zero memory allocation as I literally cconver the list of the string which can take
        # up a lot in the memory
        
        # First convert the string into a list, I really want to scan through the list of strings and check 
        # for each of the iterations
        # First check if it it's digit from len(s) <= 3
        s = s.strip()
        if not s:
            return False

        # Check if there's more than two dots and more than 2 Es in the digits 

        # We want to create boolean values, so I want to iterate through the list, and I want to check for values that are like say for niche case that has e3 or .2 which is False and True respectively so we really want to create like a boolean value to check if the  dot and E is seen
        # First convert the s into a list

        seen_E = False
        seen_dot = False
        is_a_number = False
        for i, curr in enumerate(s):
            if curr.isdigit():
                is_a_number = True 
            # For this one I am checking to see if a E is duplicated or there's no is_number before it,
            # so we can have like .E which is obv not approved or EE not approved either
            elif curr in ('e', 'E'):
                if seen_E or not is_a_number:
                    return False
                seen_E = True
                is_a_number = False 
            # We want to check for the . and see if there's a seen_dot just before the iteration or a Seen E
            # if it does it will return false, else return true
            elif curr == '.':
                if seen_dot or seen_E:
                    return False
                seen_dot = True
            elif curr in ('+', '-'):
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
            else:
                return False

        return is_a_number 
        