class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        holder = 0
        for ind in range(len(nums)):
            if nums[ind] != 0:
                nums[holder],nums[ind] = nums[ind],nums[holder]
                holder += 1
     
         
       