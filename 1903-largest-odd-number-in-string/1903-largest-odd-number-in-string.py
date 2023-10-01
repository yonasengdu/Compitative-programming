class Solution:
    def largestOddNumber(self, num: str) -> str:
      
        right = len(num)  
        for i in range(len(num) - 1,-1,-1):
            if int(num[i]) % 2 == 0:
                right -= 1 
            else:
                break
                
                
        return num[:right]
            
        