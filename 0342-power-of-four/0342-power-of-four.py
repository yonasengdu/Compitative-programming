class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return  1
        elif n < 1:
            return False
        return self.isPowerOfFour(n/4)
        