class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        ans = []
        
     
        while len(ans) < len(s):
            for i in range(97,123):
                char = chr(i)
                if count[char] > 0:
                    ans.append(char)
                    count[char] -= 1
                    
            for i in range(122,96,-1):
                char = chr(i)
                if count[char] > 0:
                    ans.append(char)
                    count[char] -= 1
                    
        return ''.join(ans)
                    
     
                 
                        
                        
                    
                        
                    