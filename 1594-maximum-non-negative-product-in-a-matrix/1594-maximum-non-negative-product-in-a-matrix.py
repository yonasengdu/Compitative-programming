class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        product = float("-inf")
        
        @cache
        def dp(row,col,prod):
            nonlocal product
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                product = max(product,prod)
                return 
            
            direction = [(1,0),(0,1)]
            
            for dirct in direction:
                if inbound(row+dirct[0],col+dirct[1]):
                    dp(row+dirct[0],col+dirct[1],prod*grid[row+dirct[0]][col+dirct[1]])
                                
        dp(0,0,grid[0][0])
        
        if product >=  0:
            return product % (10**9 + 7)
        else: return -1
            
                
                
            