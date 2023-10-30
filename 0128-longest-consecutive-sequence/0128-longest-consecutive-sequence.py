class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        heapify(nums)
        
        ans = 0
        temp = 0
        
        prev = float('inf')
        for idx in range(length):
            top = heappop(nums)
            diff  = abs(top - prev )
            if  diff > 1:
                ans = max(ans,temp)
                temp = 0
            
             
            prev = top
            if diff > 0:
                temp += 1
            
        return max(ans,temp)
            
    
            
            
                
                
            
            

        