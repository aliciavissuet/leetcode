class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    matrix = self.set_row_x(matrix, i)
                    matrix = self.set_col_x(matrix, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='X':
                    matrix[i][j]=0
                
                    
    def set_row_x(self, matrix, row):
        for col in range(len(matrix[row])):
            if matrix[row][col]!= 0:
                matrix[row][col] = 'X'
        return matrix
    
    def set_col_x(self, matrix, col):
        for row in range(len(matrix)):
            if matrix[row][col]!= 0:
                matrix[row][col] = 'X'
        return matrix