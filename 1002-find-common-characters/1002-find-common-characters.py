class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for char in ascii_lowercase:
            ctr = float("inf")
            for word in words:
                temp_count = word.count(char)
                if temp_count < ctr:
                    ctr = temp_count
            ans.extend([char]*ctr)
        
        return ans
            
          
                           
                
                
        