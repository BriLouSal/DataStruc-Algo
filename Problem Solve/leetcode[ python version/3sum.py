class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use a pointers, but unlike 2sums, we'd put the pointers inside of the 
        # iteration because we're 
        
        list_num = []
        nums.sort()
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            left = x + 1
            right = len(nums) - 1
            while left < right:
                iteration = nums[x] + nums[left] + nums[right]
                if iteration == 0:
                    list_num.append([nums[x], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                elif iteration < 0:
                    left += 1
                else:
                    right -= 1
        return list_num