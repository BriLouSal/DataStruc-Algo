class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        sorted_nums_permutation = []
        for i in range(len(nums)):
            sorted_nums_permutation.append(nums[nums[i]])
        return sorted_nums_permutation
