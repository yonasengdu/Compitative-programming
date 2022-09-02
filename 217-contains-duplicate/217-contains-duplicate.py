class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        value = nums[0]
       
        for i in range(1,len(nums)):
            if nums[i] == value:
                return True
            value =  nums[i]
        return False
            
        