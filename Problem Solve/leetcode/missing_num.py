class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Formula  (N*(N+1)/2) - Sum(nums) 
        # let N = the length of the list
        return  (n * (n + 1) // 2 ) - sum(nums) 
    