class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        set_val = set()
        
        
        for end in range(len(s)):
            while s[end]  in set_val:
                set_val.remove(s[start])
                start += 1
            set_val.add(s[end])
            length = max(length, end - start + 1)
        return length
        
                
            
            