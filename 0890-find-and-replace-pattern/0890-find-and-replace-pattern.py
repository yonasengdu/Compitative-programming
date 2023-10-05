class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        count = len(set(pattern))
       
        ans = []
        for word in words:
            mapper = {}
            
            if len(word) > len(pattern):
                continue
                
            converted = []
            for i in range(len(word)):
                if pattern[i] not in mapper:
                    mapper[pattern[i]] = word[i]
                    
                converted.append(mapper[pattern[i]])
            
           
            if ''.join(converted) == word and count == len(set(word)):
                ans.append(word)
                
                
        return ans
                    
                    
                
                
            
            
           
              
                
        
