class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        self.ans = 0
        
        def isValid(row,col):
            return (0 <= row <  len(grid2)) and (0 <= col < len(grid2[0])) and grid2[row][col] == 1
               
        
        def dfs(row,col,path):
            
          
            
          
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
           
            grid2[row][col] = 0
            
            for dr,dc in directions:
                newrow = row + dr
                newcol = col + dc
                if isValid(newrow,newcol):
                    path.append((newrow,newcol))
                    dfs(newrow,newcol,path)
                    
                    
            return path
                    
                    
                
                
                
            
            
        
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if isValid(row,col):
                    valid = [(row,col)]
                else:
                    valid = []
                    
                if grid2[row][col] == 1:
                    flag = True
                    newpath = dfs(row,col,valid)
                    
                    for x,y in newpath:
                        if grid1[x][y] != 1:
                            flag = False
                            break
                            
                    if flag:
                        self.ans += 1
                    
                   
             
        return self.ans
