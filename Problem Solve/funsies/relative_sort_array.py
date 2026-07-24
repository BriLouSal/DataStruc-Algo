class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        order_lookup = {num: i for i, num in enumerate(arr2)}
        def sort_key(num):
            if num in order_lookup:
                return (0, order_lookup[num]) 
            else:
                return (1, num)  
        return sorted(arr1, key=sort_key)