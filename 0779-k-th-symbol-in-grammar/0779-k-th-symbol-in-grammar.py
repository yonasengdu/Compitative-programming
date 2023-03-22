class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        mid = ceil(2**(n - 1) / 2)
        if n == 0:
            return 0
        
        if mid >= k:
            return self.kthGrammar(n - 1, k)
        else:
            return self.kthGrammar(n - 1, k - mid) ^ 1
        
   
            
            
        