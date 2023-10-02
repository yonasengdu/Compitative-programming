class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        
        ans = 0
        for word in words:
            allIn = True
            for char in word:
                if char not in allowed:
                    allIn = False
                    break
            if allIn:
                ans  += 1
                
        return ans
                    
        