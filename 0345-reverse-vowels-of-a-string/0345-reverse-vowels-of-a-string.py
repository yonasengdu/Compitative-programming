class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        s = list(s)
        
        while left <= right:
            if s[left] not in vowels:
                left += 1
                
            elif s[right] not in vowels:
                right -= 1
            
            else:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
                
        return "".join(s)