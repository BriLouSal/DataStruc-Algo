class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        new_list = [x for item in grid for x in item]
        N = len(new_list) 
        new_list.sort()
        l = None
        for i in range(len(new_list) - 1):
            if new_list[i] == new_list[i + 1]:
                l = new_list[i]
                break
            else:
                continue
        # Because of inflated sum
        j = (N * (N + 1) // 2 ) - (sum(new_list) - l)
        return [l,j]
        # a mix of missing number and duplicate number