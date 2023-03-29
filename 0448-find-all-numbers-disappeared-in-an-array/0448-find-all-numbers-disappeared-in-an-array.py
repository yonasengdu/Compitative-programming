class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        left = 0
        ans = []
        
        while left < len(nums):
                
            swap = nums[left]
            if nums[left] == nums[swap - 1]:
                left += 1
                continue
                
            nums[left],nums[swap - 1] = nums[swap - 1],nums[left]
            
            if left == swap - 1:
                left += 1
            
            
      
        for ind in range(len(nums)):
            if nums[ind] != ind + 1:
                ans.append(ind + 1)
                
        return ans