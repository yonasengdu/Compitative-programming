class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            def checker(row,col):
                new_arr = []
                val = [(0,0),(0,1),(0,2),(1,0),(2,0),(1,1),(1,2),(2,1),(2,2)]
                for i,j in val:
                    newRow = row + i
                    newCol = col + j
                    new_arr.append(board[newRow][newCol])
                count_new_arr = Counter(new_arr)
                for val,num in count_new_arr.items():
                    if val != "." and num > 1:
                        return True
                return False

            for ind in range(9):
                row = board[ind]
                col = []
                for jnd in range(9):
                    col.append(board[jnd][ind])
                count_row = Counter(row)
                count_col = Counter(col)
                for val,num in count_row.items():
                    if val != "." and num > 1:
                        return False
                for val,num in count_col.items():
                    if val != "." and num > 1:
                        return False

            for ind in range(0,9,3):
                if checker(0,ind) or checker(3,ind) or checker(6,ind):
                    return False
            return True
                
                
                
          

            
            
                