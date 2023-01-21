class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral = []
        while matrix:
            while matrix and matrix[0]:
                val = matrix[0][0]
                spiral.append(val)
                matrix[0].remove(val)
            if matrix:
                matrix.pop(0)
            
            for row in matrix:
                if row:
                    spiral.append(row[-1])
                    row.pop()
                
            while matrix and matrix[-1]:
                val = matrix[-1][-1]
                spiral.append(val)
                matrix[-1].pop()
            if matrix:
                matrix.pop(-1)
            
            for row in reversed(matrix):
                if row:
                    spiral.append(row[0])
                    row.pop(0)
        return spiral
                
        