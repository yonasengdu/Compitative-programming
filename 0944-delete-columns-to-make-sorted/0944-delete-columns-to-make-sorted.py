class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        ans = 0
        for i in range(n):
            check = 96
            for word in strs:
                if ord(word[i]) >= check:
                    check = ord(word[i])
                else:
                    ans+= 1
                    break
                    
                    
        return ans
        
                    
                
                
        