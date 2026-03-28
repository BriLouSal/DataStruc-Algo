class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # We can do a list comphrension, such as that we're getting every pairs,
        # one way we can do it is do a nested list first and then sum it per iteration
        nums.sort()
        # Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
        return max((nums[i] + nums[len(nums) - i - 1]) for i in range(len(nums) // 2))