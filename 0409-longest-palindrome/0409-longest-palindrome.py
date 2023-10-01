class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
            
            
        longest = 0    
        for latter,count in count.items():
            if count % 2 == 0:
                longest += count
                
            elif count > 2:
                longest += count - 1
                
        return longest if longest == len(s) else longest + 1

        