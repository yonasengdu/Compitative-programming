class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [1] + [0]*(amount)

        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]
                
        
        
        
#         @cache
#         def dp(idx,total):
#             if total == amount:
#                 return 1
                
#             if total > amount or idx == len(coins):
#                 return 0
            
#             return dp(idx,total + coins[idx]) + dp(idx + 1,total)
                
#         return dp(0,0)  