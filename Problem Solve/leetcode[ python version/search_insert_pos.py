class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # A placeholder to check for num, make sure we have to do is 
        # if the target is not in the list, we can use our place holder to check
        # that if it doesn't exist, then we can just do a sort() and then find where we can 
        # insert it, first we do binary search
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
                

        return l