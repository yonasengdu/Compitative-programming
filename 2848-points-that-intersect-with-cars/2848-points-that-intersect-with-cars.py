class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        
        theMax = 0
        
        for x,y in nums:
            theMax = max(theMax,x,y)
            
        prefix = [0]*(theMax+2)
        
        for x,y in nums:
            prefix[x] += 1
            prefix[y+1] -= 1
            
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i - 1]
            
            
        zeros = prefix[1:-1].count(0) 
       
        return theMax - zeros