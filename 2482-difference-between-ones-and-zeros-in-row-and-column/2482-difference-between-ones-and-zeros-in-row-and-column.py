class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        val_1 = {}
        val_2 = {}
        for rows in range(len(grid)):
            onesRow = 0
            zerosRow = 0
            row = grid[rows]
            for value in row:
                if value == 0:
                    zerosRow += 1
                else:
                    onesRow += 1
            val_1[rows] = [onesRow , zerosRow]
        
      
        for num in range(len(grid[0])):
            temp_ans = []
            onesCol = 0
            zerosCol = 0
            for row in grid:
                if row[num] == 0:
                    zerosCol += 1
                else:
                    onesCol += 1
   
            val_2[num] = [onesCol,zerosCol]
        for rows in val_1.values():
                onesRow = rows[0]
                zerosRow = rows[1]
                temp_ans = []
                for col in val_2.values():
                    onesCol = col[0]
                    zerosCol = col[1]
                    
                    diff = onesRow +   onesCol - (zerosRow + zerosCol)
                    temp_ans.append(diff)
                    
                ans.append(temp_ans)
        return ans
                    
                
      
            
         
                        

                        
                
        