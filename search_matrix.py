def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.search_helper(matrix, target, 0, 0)
    def search_helper(self, matrix, target, row, col):
        if len(matrix[row])==0:
            return False
        curr = matrix[row][col]
        
        if curr=='X':
            return False
        if curr == target:
            return True
        if curr > target:
            matrix[row][col] = 'X'
            if row > 0:
                left = self.search_helper(matrix, target, row-1, col)
            else:
                left = False
            if col > 0:
                up = self.search_helper(matrix, target, row, col-1)
            else:
                up = False
            return (left and up)
        else:  
            matrix[row][col] = 'X'
            if row < len(matrix)-1:
                right = self.search_helper(matrix, target, row+1, col)
            else:
                right = False
            if col < len(matrix[row])-1:
                up = self.search_helper(matrix, target, row, col+1)
            else:
                up = False
            return (up or right)
