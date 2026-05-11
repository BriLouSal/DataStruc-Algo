class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Same as combination, we're clearly using backtracking, combinations of subsets
        # where we use recursion
        result = []
        def backtracking(start, path):
            result.append(list(path))
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()


        backtracking(0, [])
        return result