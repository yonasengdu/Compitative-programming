class Solution:
    def maximum69Number (self, num: int) -> int:
        digits  = []
    
      
        while num > 0:
            digits.append(str(num%10))
            num //= 10
        digits = digits[::-1]  
        for i in range(len(digits)):
            if digits[i] == "6":
                digits[i] = "9"
                break
        
          
        return (int("".join(digits)))

                
            