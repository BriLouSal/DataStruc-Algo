class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Can't we just do a set on that nums and then sort it LOL, I was overcomplicating it LOL
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)