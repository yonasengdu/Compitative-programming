class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                
        self.ans = 0
        
        def isValid(row,col):
            return (0 <= row <  len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == 1
               
        
        def dfs(row,col):
            
            grid[row][col] = 0
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            self.temp += 1
            for dr,dc in directions:
                newrow = row + dr
                newcol = col + dc
                if isValid(newrow,newcol):
                    dfs(newrow,newcol)
                    
                    
                
                
                
            
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.temp = 0
                    dfs(row,col)
                    self.ans = max(self.ans,self.temp)
                    
        return self.ans

                