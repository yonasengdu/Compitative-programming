class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
       
        if sum(gas) < sum(cost):
            return -1
        
       
        curr  = 0
        left = 0
        for i in range(n):
            diff = gas[i] - cost[i]
          
            curr += diff
            
            if curr < 0:
                left = i + 1
                curr = 0
                
           
            
            
     
        
        return left 
            
            
           
            
            
        
        
        