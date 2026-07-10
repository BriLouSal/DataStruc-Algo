class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # We can easily make a counter for each time an array appears via a hashmap
        counter = {}
        for item in nums:
            if item in counter: 
                counter[item] += 1
            else:
                counter[item] = 1
        # and then we can do is iterate through the hashmap and make a variable
        # called unique_value where we can see if we get a items that has an equal of 1
        unique_value = None
        for item, count in counter.items():
            if count == 1:
                unique_value = item
                
        return unique_value