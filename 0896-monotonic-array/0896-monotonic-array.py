class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc = False
                
        dec = True       
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                dec = False
                
        return inc | dec
                
            
       
        