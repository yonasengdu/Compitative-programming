class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob(nums):
            x = 0
            y =  0
            
            for i in range(1,len(nums)):
                x, y = y+nums[i], max(x,y)
                
            return max(x,y)
                
        if len(nums) == 1:
            return nums[0]
        else:
            return max(rob(nums),rob(nums[::-1]))
        
        
        