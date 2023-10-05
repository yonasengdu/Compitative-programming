class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        shouldHappen = len(nums) // 3
        nums.sort()
        
        left = 0
        
        ans = []
        
        for right in range(len(nums)):
            
            if nums[left] != nums[right]:
                print
                if right - left > shouldHappen:
                    ans.append(nums[left])
                left = right
                
        if len(nums) - left > shouldHappen:
            ans.append(nums[left])
            
        return ans
                
        
       
        
        
        