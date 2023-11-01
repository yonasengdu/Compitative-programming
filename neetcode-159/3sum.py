class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums) - 1
        nums.sort()
        
        ans = set()
        for idx,first in enumerate(nums):
            temp_target = 0 - first
            
            left = idx + 1
            right = length
            
            while left  < right:
                diff = temp_target - nums[left]
                
                if nums[right] < diff:
                    left += 1
                    
                elif nums[right] > diff:
                    right -= 1
                    
                else: 
                    ans.add((first,nums[left],nums[right]))
                    left += 1
                    right -= 1
                    
              
                    
        return list(ans)
                    
                    
            
            
            
            
        