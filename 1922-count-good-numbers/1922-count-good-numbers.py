class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
          

        mod =  10**9 + 7
        div = n / 2 
        expo_5 = pow(5, ceil(div), mod) 
        expo_4 = pow(4,(floor(div)), mod)
        
        return expo_5 * expo_4  % mod
        
        
      