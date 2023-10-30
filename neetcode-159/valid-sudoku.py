class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        m = len(board[0])
        
        for row in board:
            row_values = Counter(row)
           
            for val,cnt in row_values.items():
                if val != '.' and cnt > 1:
                    return False
                
        for row in range(n):
            col_values = defaultdict(int)
            
            for col in range(m):
                val = board[col][row]
                col_values[val] += 1
                
            
            for val,cnt in col_values.items():
                if val != '.' and cnt > 1:
                    return False
                
        
        for row in range(0,n,3):
            for col in range(0,m,3):
                sub_mat_val = defaultdict(int)
                for sub_row in range(row,row + 3):
                    for sub_col in range(col,col + 3):
                        val = board[sub_row][sub_col]
                        sub_mat_val[val] += 1
              
                for val,cnt in sub_mat_val.items():
                    if val != '.' and cnt > 1:
                        return False
                    
                    
        return True

                
                        
                
                
            
            
        