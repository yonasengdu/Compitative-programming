class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        @cache
        def dp(idx,total):
            if total == amount:
                return 1
                
            if total > amount:
                return 0
            
            count = 0
            for i in range(idx,len(coins)):
                count += dp(i, total + coins[i])
                
            return count
                
            
        
        return dp(0,0)
                
        