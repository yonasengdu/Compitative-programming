class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = 1
        cnt_zero = 0
        
        for num in nums:
            
            if num == 0:
                cnt_zero += 1
            else:
                prefix *= num
            
            
        
        if cnt_zero > 1:
            return [0]*n
        
        elif cnt_zero == 1:
            for idx,num in enumerate(nums):
                if num != 0:
                    nums[idx] = 0
                    
                else:
                    nums[idx] = prefix
                    
        else:
             for idx,num in enumerate(nums):
                    nums[idx] = prefix // num
            

            
        return nums
        