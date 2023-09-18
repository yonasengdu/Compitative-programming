class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0]*n
        dp[0] = 1
     
        
        for i in range(2,n+1):
            n = 2*(i - 1) + 1
            curr_count = (n * (n + 1))// 2
           
            dp[i - 1] += (dp[i - 2] * curr_count)
            
        
        return dp[-1] % (10**9 + 7)
            
            