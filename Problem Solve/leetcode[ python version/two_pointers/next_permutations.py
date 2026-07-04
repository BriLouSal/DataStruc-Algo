class Solution(object):
    # Let's make a function that checks if it's lexigraphical
    def is_lexicographical(self, lst):
        str_lst = [str(x) for x in lst]
        return all(str_lst[i] <= str_lst[i + 1] for i in range(len(str_lst) - 1))
    
    def nextPermutation(self, nums):
        # So wait I see how this works, if we can just shift the code to the left.
        # However if the code in the nums is sorted asecendially, and if the
        # first iteration is the shortest number, then we'll keep it at that.
        # However the list MUST be in lexicographical order
        RIGHTMOST_INDEX = 2
        
        if self.is_lexicographical(nums[::-1]):
            nums.sort()
            return
        i = len(nums) - RIGHTMOST_INDEX
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            # Grab the j with the end_index
            END_INDEX = 1
            j = len(nums) - END_INDEX

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])