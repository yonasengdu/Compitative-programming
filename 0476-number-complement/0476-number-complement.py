class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        base = 0
        while num > 1:
            if num & 1 == 0:  
                curr_bit = 1
                result += pow(2,base) 
                
            base += 1
            num >>= 1
            
        return result
            
            
        