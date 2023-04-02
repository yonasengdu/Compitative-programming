class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        
        for ind in range(len(words)):
            curr = words[ind]
            for j in range(ind+1,len(words)):
                mobile = words[j]
          
                
                flag = True
                for char in curr:
                    if char in mobile:
                        flag = False
                        break
                if flag:
                    
                    ans = max(ans,len(curr)*len(mobile))
                    
                
        return ans
                    
            
            
        