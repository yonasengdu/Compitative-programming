class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = ord('a') 
        
        seconds = 0
        for char in word:
            cur = abs(ord(char) - prev)
            seconds += min(cur + 1, 27 - cur)
            prev = ord(char)
           
            
            
        return seconds
            
        
        