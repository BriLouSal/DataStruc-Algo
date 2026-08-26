class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Ok so in order to split the array in largest sum, we'd need to use greedy algo since we want to 
        # MINIMIZE the subarray sum, I have an idea actually, what if we just compare the two largest array and then compare it to the rest, and if it's not the largest, we add into it so dp[2] -> dp[3] and so fourth
        # and this could be a strong possibility so we can store like the candidate, we want to minimize it as possible, and  k is the biggest possible, so the question is we can only split the largest subarray as k length, so exactly at k
        left = max(nums)
        right = sum(nums)

        # So we wanna do a binary search
        while right > left:
            mid = (left + right) // 2
            # Counter for candidiate for the max, and sub
            curr = 0
            sub = 1

            for i in nums:
                if curr + i  > mid:
                    # Subarray is added, and we store the largest candididate number
                    curr = i 
                    sub += 1
                else:
                    curr += i
            # Now we check if the subarray is actually smaller than k, if so we know that need larger max
            if sub <= k:
                right = mid
            else:
                left = (mid + 1)
        return left
