from itertools import permutations
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        left = 0
        right = len(s)
        ans = []
        
        for char in s:
            if char == "I":
                ans.append(left)
                left+= 1
            else:
                ans.append(right)
                right -= 1
                
                
        ans.append(left)
        
        return ans
                
        
            
        