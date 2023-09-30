class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = ''.join(sorted(s))
    
        return   s[:-1][::-1] + s[-1]
        
        