class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []
        
        def collectTheBoundery(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == "O":
                        if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) -1:
                            stack.append((row,col))
                            
        def is_valid(node):
            return ( 0 <= node[0] < len(board)) and (0 <= node[1] < len(board[0])) and (board[node[0]][node[1]] == "O")
                            
        def dfs(node):
            
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            board[node[0]][node[1]] = "F"
            
            for dr,dc in directions:
                new_pos = (node[0]+dr,node[1]+dc)
                if is_valid(new_pos):
                    dfs(new_pos)
                    
                
                
                
        collectTheBoundery(board)               
        for node in stack:
            dfs(node)
            
        for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == "O":
                        board[row][col] = "X"
                        
                        
        for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == "F":
                        board[row][col] = "O"
                        
                    
                        

