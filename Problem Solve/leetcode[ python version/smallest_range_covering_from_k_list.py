import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # So for this one we have a linked List, well we're looking for the smallest range
        # The question defines range [a,b] smaller than [c,d] so one way is that
        # if (b-a) < [d-c] or a < c elif (b-a) == (d-c)

        # FURTHERMORE WE WANT: non-decreasing order as our answer
        # This question is primarily to optimize the width of the rnage, so that's why we ignore 26
        # and use 24 since 24 - 20 means smaller width

        # To hold our solution
        list_of_sets = []
        # Hold a value of smallest_range and biggest_range
        biggest_val = float('-inf')
        # Use enumeration to get the value of the entire list, and find the biggest val and val[0] cabn be used to
        # assume the smallest number
        for index, arr in enumerate(nums):
            val = arr[0]
            heapq.heappush(list_of_sets, (val, index, 0))
            biggest_val = max(biggest_val, val)
        start = list_of_sets[0][0]
        end = biggest_val


        while True:
            mins, ind, el_ind,= heapq.heappop(list_of_sets)
            # Let mins = a, Let b  = ind, let c = start, let d = end
            a = mins 
            b = biggest_val 
            c = start
            d = end
            if((b-a) < (d-c)) or ((b-a) == (d-c)) and a < c:
                start = a
                end = b
            index_next = el_ind  + 1
            if index_next == len(nums[ind]):
                break

            next_value = nums[ind][index_next]
            heapq.heappush(list_of_sets, (next_value, ind, index_next))
            biggest_val = max(biggest_val, next_value)
        
        return [start, end]