class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        prep = []
        for i,tap in enumerate(ranges):
            start = i - tap
            end = i + tap
            
            if start < 0:
                start = 0
            
            prep.append([start ,end])
            
        prep.sort()
        
        stack = []
        
  
        if prep[0][0] > 0:
            return -1
        else:
            stack.append(prep[0])
           
        
        checker = 0
        for i in range(len(prep)):
            start = prep[i][0]
            end = prep[i][1]
            
            if start > stack[-1][1]:
                return -1
            
            if stack[-1][-1] >= n:
                return len(stack)
                
            i = -1
            if start <= checker and end > stack[-1][1]:
                stack[-1] = [start,end]
                
            if start <= stack[-1][1] and end > stack[-1][1] and start > stack[-1][0]:
                checker = stack[-1][1] 
                stack.append([start,end])
           
                
                
                
           
                
            
            
            
            
        return len(stack)
    
            
            
   
        
                
                
    
                
            
                
                
            
        
        
            
                
                
        
        
       
        
  
            
            
        
       
            
        
                            
          
                
                
            
        
                 