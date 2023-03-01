class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        totalShifts = [0] * (n + 1)
        ans = []
        
        #setting up to calculate how much shift happens for every latter
        for shiftArray in shifts:
            startInd = shiftArray[0]
            endInd = shiftArray[1]
            direction = shiftArray[2]
            
            if direction == 0:
                totalShifts[startInd] += -1
                totalShifts[endInd + 1] += 1
            else:
                totalShifts[startInd] += 1
                totalShifts[endInd + 1] += -1
                
        # calculating the shifts for every latter
        for ind in range(1,n + 1):
            totalShifts[ind] += totalShifts[ind - 1]
            
    
        ## conversion
        for ind in range(n):
            ascii_val_latter = ord(s[ind])
            amount_latter_shift = totalShifts[ind] % 26
            ascii_latter_after_shift = ascii_val_latter + amount_latter_shift   
            
            if  ascii_latter_after_shift > 122:
                 ascii_latter_after_shift = 96 + ascii_latter_after_shift % 122
                    
            latter_after_shift = chr(ascii_latter_after_shift) 
            ans.append( latter_after_shift)
        
        
        return "".join(ans)
           
                
            
        
        
        
        
        
            
        
                
        