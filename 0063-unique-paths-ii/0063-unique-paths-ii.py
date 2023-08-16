class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
       
        def valid(row,col):
            return 0 <= row < len(obstacleGrid) and 0 <= col <len(obstacleGrid[0])
        
        @cache
        def count(row,col):
            if row == len(obstacleGrid) - 1  and col == len(obstacleGrid[0]) - 1:
                return 1
            
            if not valid(row,col):
                return 0
            
            if valid(row,col) and obstacleGrid[row][col] == 1:
                return 0
            
            return count(row + 1,col) + count(row,col + 1)
            
          
        
        
        return count(0,0)
            
        
            
        
        
        