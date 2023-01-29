class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left,right+1):
            flag = False
            for ind in str(num):
                if  "0" not in str(num):
                    if num % int(ind) != 0:
                        flag= False
                        break
                    else:
                        flag = True
                else: 
                    flag = False
            if flag:
                ans.append(num)
        return ans
            
                
                    
            
            
       
        
            
        
            
        