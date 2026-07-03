class Solution(object):
    def permute(self, nums):
        # This is jutt a back tracking question, so we'd just have 
        # argument of empty list 
        args_list = []
        length_of_args = len(nums)
        visited = set()
        def backtrack(list_of):
            # So if this the index is equal to the length
            if len(list_of) == length_of_args:
                args_list.append(list_of[:])
                return
            for num in nums:
                if num in list_of:
                    continue
                visited.add(num)
                list_of.append(num)
                backtrack(list_of)

                list_of.pop()
                visited.remove(num)
        backtrack([])
        return args_list