class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def uniquePath(row , col,memo=defaultdict(int)):
            if not ((0 <= row < m) and (0 <= col < n)):
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            
            if (row,col) == (0,0):
                return 1
            
            memo[(row,col)] = uniquePath(row - 1,col,memo) + uniquePath(row ,col -1,memo)
            return memo[(row,col)]
        
        return uniquePath(m - 1,n - 1)
        
        
            
        