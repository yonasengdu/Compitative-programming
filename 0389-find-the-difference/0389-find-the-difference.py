class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        str_1 = sorted(s)
        str_2 = sorted(t)
        
        for i in range(len(s)):
            if str_1[i] != str_2[i]:
                return str_2[i]
            
        return str_2[-1]
            
        