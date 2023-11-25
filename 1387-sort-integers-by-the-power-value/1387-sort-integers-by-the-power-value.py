class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        power_values = []
        for num in range(lo,hi+1):
            transform = num 
            steps = 0
            while transform != 1:
                if transform % 2 == 0:
                    transform = transform //  2
                else:
                    transform = 3 * transform + 1
                    
                steps += 1
                
            power_values.append((steps,num))
            
            
        power_values.sort()
        
      
        return power_values[k - 1][1]
                
        
            
        
        
        