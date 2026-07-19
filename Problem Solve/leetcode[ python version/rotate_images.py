class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # This is just tranposing  matrix so the rows will be rotated to columns 
        
        # So it would be matrix[i][j] -> matrix[j][i], this is pretty easy
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # This will actually lead to higher runtime speed due to the reverse nature, as in the underneath
        # There's C code that makes it super optimized, but we don't really have to learn this till CPSC 355
        # So we'll be using reverse for this haha, and this is how we do it: Reverse the row since we'll have it 
        # at like a 90 degrees, look at this row 1 is initally [1,4,7]
        # But after the rotation, we have [7,4,1] 
        for row in matrix:
            row.reverse()
            
            
    