class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        small = Counter(s1)
        
        
        left = 0
        right = len(s1)
        
        large = Counter(s2[left:right])
        
        if small == large:
                return True
            
        while right < len(s2): 
            large[s2[left]] -= 1
            
            if not large[s2[left]]:
                del large[s2[left]]
                
            large[s2[right]] += 1
            
            left += 1
            right += 1
            # print(large)
            if small == large:
                return True
        return False
                
            
        
        
            
        
        