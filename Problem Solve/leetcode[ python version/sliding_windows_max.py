import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # What we know, we have to grab the indexes such as k 
        # and max the list inside of it, 
        # and then append it, 
        heap = []
        list_of_max = []
        # We can use heap to bypass this as we'll have memory, and we can just
        # do one operation instead for the 1000 cases
        for i in range(len(nums)):
            # new_list = nums[i : i + k]
            # Push current num
            heapq.heappush(heap, (-nums[i], i))
            if i >= k -1:
                # This is my max logic, check for old iwndows
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                list_of_max.append(-heap[0][0])
        return list_of_max
    
# FINALLY SOLVED THIS ONE LOL, TOOK ME A WHILE AND  I NEEDED TO LOOK UP HOW TO FIX THAT time limit ERROR, BUT I FINALLY GOT IT! 
# Original Code:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # What we know, we have to grab the indexes such as k and max the list inside of it,
        # and then append it, 
        list_of_max = []
        for i in range(len(nums) - k + 1):
            new_list = nums[i : i + k]
            max_list = max(new_list)
            list_of_max.append(max_list)
        return list_of_max