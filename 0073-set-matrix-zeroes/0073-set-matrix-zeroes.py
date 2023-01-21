class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        modifier_row = []
        modifier_col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    modifier_row.append(i)
                    modifier_col.append(j)
                    
        for ind in modifier_row:
            for zero_ind in range(len(matrix[0])):
                matrix[ind][zero_ind] = 0
        for ind in modifier_col:
            for zero_ind in range(len(matrix)):
                matrix[zero_ind][ind] = 0
                
        
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        