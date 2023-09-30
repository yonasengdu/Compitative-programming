class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_minute = (int(current[0] + current[1]) * 60) + int(current[3] + current[4])
        correct_minute = (int(correct[0] + correct[1]) * 60) + int(correct[3] + correct[4])
        
        
        minute = correct_minute - current_minute
        
              
        minute_ops = 0
        while minute > 0:
            if minute >= 60:
                minute -= 60
                
            elif minute >= 15:
                minute -= 15
                
            elif minute >= 5:
                minute -= 5
                
            else:
                minute -= 1
                
            minute_ops += 1
            
       
        return minute_ops
                
                
                
                
        
        
        
        
        
        