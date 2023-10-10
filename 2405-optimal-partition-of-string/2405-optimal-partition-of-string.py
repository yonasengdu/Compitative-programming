class Solution:
    def partitionString(self, s: str) -> int:
        
        
        cheacker = set()
        subStrings = 0
        
        for char in s:
            if char in cheacker:
                subStrings += 1
                cheacker = set()
                
            cheacker.add(char)
         
        # print(cheacker)
        return subStrings + 1
                
            
            
            
        