class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # So we wanna create like a pair of two digits, etc. so we can have like a empty integer that handles the max
        # number, we can sort the list and for loop via the step 2 since IT'S ASKING FOR PAIRS, I THINK I GOT IT
        nums.sort()
        return sum(nums[::2])