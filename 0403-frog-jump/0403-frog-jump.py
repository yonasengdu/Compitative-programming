class Solution:
    def canCross(self, stones: List[int]) -> bool:
        possible = set(stones)
        
        found = False
        @cache
        def dp(pos,k):
            nonlocal found
            if pos == stones[-1]:
               
                found = True
                return 

            jumps = [k - 1, k ,k + 1]
            
            for jmp in jumps:
                if jmp > 0 and (pos + jmp) in possible:
                    dp(pos + jmp,jmp)
            
            return found
            
            
        
        return dp(stones[0],0)
                    