class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(i, idx):
            if idx >= len(triangle[i]):
                return 0
            
            if i == len(triangle) - 1:
                return triangle[i][idx]
            
            return min(triangle[i][idx] + dp(i + 1, idx) , triangle[i][idx] + dp(i + 1, idx + 1))
        
        return dp(0, 0)