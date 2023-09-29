class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0, 0
        
        ans = 0
        for char in s:
            if char == "L":
                left += 1
            elif char == "R":
                right += 1
                
            if left == right:
                ans += 1
                
        return ans
                
        