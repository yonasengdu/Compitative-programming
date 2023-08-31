class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        
        @cache
        def dp(idx,time):

            if idx == len(satisfaction):
                return 0
         
            return max(satisfaction[idx] * time + dp(idx + 1,time + 1),dp(idx + 1,time))
          
          
     
        return    dp(0,1)
        