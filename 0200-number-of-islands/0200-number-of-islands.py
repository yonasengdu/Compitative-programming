class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        
        def isValid(row,col):
            return (0 <= row <  len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1"
               
        
        def dfs(row,col):
            grid[row][col] = 0
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for dr,dc in directions:
                newrow = row + dr
                newcol = col + dc
                if isValid(newrow,newcol):
                    dfs(newrow,newcol)
                    
                
                
                
            
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row,col)
        return ans
                    
        