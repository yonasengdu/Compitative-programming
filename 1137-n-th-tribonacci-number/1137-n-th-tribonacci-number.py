class Solution:
    def tribonacci(self, n: int) -> int:
        ggp , gp , p   = 0,1,1
         
        if 0 < n <= 2:
            return 1
        if n == 0:
            return 0
        
        for i in range(3,n+1):
            curr = ggp + gp + p
            ggp = gp
            gp = p
            p = curr
            
        
        return curr  