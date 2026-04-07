class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # So for this one we'd probably want to create like a
        # string manipulation technique, check if that string exists
        # in the modified_list (which we return), and we can do upper
        # for each of them, assuming that s is lower case
        s = s.lower()
        modified_string_perm = []
        # iterate through s, and we'll modify per case right, and we append
        # via converting the s back into the string and check if they're in the list already
        # if not append, else continue and do not append
        s_list = list(s)
        modified_string_perm.append(s)
        for i in range(len(s)):
            # Check is alphabetic, if it is, we can do the upper case and append to the modified_string_perm
            if s[i].isalpha():
                size_of_string = len(modified_string_perm)
                for j in range(size_of_string):
                    modifier = list(modified_string_perm[j])
                    modifier[i] = modifier[i].upper()
                    modified_string_perm.append("".join(modifier))
        return modified_string_perm