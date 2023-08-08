class Solution:
    def rob(self, nums: List[int]) -> int:
        x = 0
        y= nums[0]
        
        for i in range(1,len(nums)):
            x ,y = y ,max(x+nums[i],y)
            
        return y
        
        
        