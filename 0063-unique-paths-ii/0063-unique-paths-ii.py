class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
       
        def valid(row,col):
            return 0 <= row < len(obstacleGrid) and 0 <= col <len(obstacleGrid[0])
        
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = "x"
                    
        obstacleGrid[0][0] = 1
                    
                    
        for r in range(row):
            for c in range(col):
                top_row = r - 1
                left_col = c - 1
                
                if obstacleGrid[r][c] == "x":
                    obstacleGrid[r][c] = 0
                    continue
                
                if valid(top_row,c):
                    obstacleGrid[r][c] += obstacleGrid[top_row][c]
                
                if valid(r,left_col):
                    obstacleGrid[r][c] += obstacleGrid[r][left_col]
                    
        return obstacleGrid[-1][-1]
                    
                    
            
        
            
        
        
        