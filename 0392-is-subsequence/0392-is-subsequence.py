class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == '':
            return True
    
            
        left = 0
        
        for right in range(len(t)):
            if t[right] == s[left]:
                left += 1
                
            if left >= len(s):
                break
                
        if left == len(s) :
            return True
        else:
            return False
            
        