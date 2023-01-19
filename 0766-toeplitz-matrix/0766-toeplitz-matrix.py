class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for row in range(len(matrix)):
            for ind in range(len(matrix[row])):
                rind = row
                cind = ind
                diff = abs(rind - cind)
                diagonal = matrix[rind][cind]
                while rind < len(matrix) and cind < len(matrix[row]):
                    if abs(rind - cind)  == diff and matrix[rind][cind] != diagonal:
                        return False
                    rind += 1
                    cind += 1
        return True

                                
                         
                         
            