class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        prev = 0
        
        alice = 0
        bob = 0
        for i in range(len(colors)):
            if colors[i] != colors[prev]:
                if colors[prev] == "A":
                    alice += max(0, i - prev - 2)
                else:
                    bob += max(0, i - prev - 2)
                    
                prev = i
         
        if prev < len(colors) - 1:
            if colors[prev] == "A":
                alice += max(0,len(colors) - prev - 2)
            else:
                bob += max(0,len(colors) - prev - 2)
                
                
          
        return True if alice > bob else False
                
            
            
        