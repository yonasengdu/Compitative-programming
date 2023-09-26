class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones) 
        target = ceil(total / 2)
        
        
        @cache
        def dp(idx , tally):
            if idx >= len(stones) or tally >= target:
                return abs(2 * tally - total) 
            
            return min(dp(idx + 1, tally) , dp(idx + 1,tally + stones[idx]))
      
        return dp(0,0)
        