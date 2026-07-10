class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # This is pretty easy lol, all we have to do is make a variable
        # does_exist and then we iterate through the nested array, and check
        # if the target exist, but if visited is equals to the length of matrix
        # and we haven't found it yet, then we do does_exist = False and then break the for loop
        does_exist = False
        for i in range(len(matrix)):
            visited = 0
            if target in matrix[i]:
                does_exist = True
                break
            elif visited == len(matrix) + 1:
                does_exist = False
                break

            else: 
                continue
                visited += 1
        return does_exist