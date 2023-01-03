
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        val_row= {}
        val_col = {}
        total =0
        for index in range(len(grid)):
            val_row[index]=grid[index]
            col = []
            for el in grid:
                col.append(el[index])
            val_col[index] = col
        for row_ptr in range(len(val_row)):
            for col_ptr in range(len(val_row)):
                if val_row[row_ptr] == val_col[col_ptr]:
                    total += 1
        print(val_row,val_col)
                
        return total
            
            
          
        
 