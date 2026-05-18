from collections import Counter
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # So for this situation we'd probably want to not use subarray due to Memory limit array
        # such as the limti is  N = 20,000. So accordinf to the hint, we would want to do a two pointer 
        #  and use the formula Atmost(K) - Atmost(K - 1)
        def atMost(goal: int) -> int:
            if goal < 0:
                return 0
            count = Counter()
            left = 0
            total_subarrays = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    goal -= 1
                count[nums[right]] += 1
                while goal < 0:
                    # While the goal
                    count[nums[left]] -= 1
                    # If the nums to the left is 0 increase the goal increment
                    if count[nums[left]] == 0:
                        goal += 1
                    left += 1
                    # Increase the increment by right index - (left+1)
                total_subarrays += (right - left + 1)
            return total_subarrays
        return atMost(k) - atMost(k - 1)