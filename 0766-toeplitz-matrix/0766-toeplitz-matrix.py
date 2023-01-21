class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:  
        for row in range(len(matrix)-1):
            for ind in range(len(matrix[row])-1):
                if matrix[row][ind] != matrix[row+1][ind+1]:
                    return False
        return True
                 
                         
            