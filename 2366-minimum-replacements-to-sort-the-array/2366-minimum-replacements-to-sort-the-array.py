class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        prev = nums[-1]
        steps = 0
        
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > prev:
                
                temp = ceil(nums[i]/prev) 
                prev = nums[i]//temp
                steps += temp - 1
                
            else:
                prev = nums[i]
                
            
        return steps     
            
                