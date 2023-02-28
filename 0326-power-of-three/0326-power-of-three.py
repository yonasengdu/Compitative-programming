class Solution:
    def isPowerOfThree(self, n: int) -> bool:
         if n == 1:
            return  1
         elif n < 1:
            return False
         return self.isPowerOfThree(n/3)
        
        