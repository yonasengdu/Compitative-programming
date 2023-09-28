class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[right],nums[left] = nums[left],nums[right]
                left += 1
                
        return nums
        