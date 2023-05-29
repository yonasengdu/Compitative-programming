class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        note_5,note_10,note_20 = 0,0,0
        
        for pay in bills:
            if pay == 5:
                note_5 += 1
                
            elif pay == 10:
                if note_5 == 0:
                    return False
                
                else: 
                    note_5 -= 1
                    note_10 += 1
                    
            elif pay == 20:
                if note_5 == 0:
                    return False
                elif note_10 == 0 and note_5 < 3:
                    return False
                
                else:
                    if note_10 == 0:
                        note_5 -= 3
                        note_20 += 1
                        
                    else:
                        note_10 -= 1
                        note_5 -= 1
                        note_20 += 1
                         
            
        return True


                
        