class Solution:
    def myAtoi(self, s: str) -> int:
       
        # remove any leading and trailing white space 
        s = s.strip()
        
        # check for the precence of sign
        left = 0
        sign = "+"
        if s and (s[0] == "+" or s[0] == "-"):
            sign = s[0]
            left += 1
            
        integers = []
        n = len(s)
        
        # collect all integers util no integer charachter
        for idx in range(left,n):
            if not s[idx].isdecimal():
                break
                
            integers.append(s[idx])
            
        # ignoring leading zeros
        int_start = 0
        while int_start < len(integers):
            if integers[int_start] != "0":
                break
               
                
            int_start += 1
            
            
        # preparing the magnitude integer
        integer = "".join(integers[int_start:])
        
        
       
        if not integer:
            return 0
        
        if sign == "-":
            integer = -1 * int(integer)
        else:
            integer = int(integer)
            
        
        
        # setting the bound
        if integer:
            if integer > 2**31 - 1:
                integer =  2**31 - 1
                
                
            elif integer < -1 * 2**31:
                integer = -1  * 2**31
                
        
    
        
        return int(integer)
        
                
            
        
            
        
            
            
            
            
    
        
        
        
    
                
            
                
                
        