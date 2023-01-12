class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for num_index in range(len(nums)-1):
            val_first = nums[num_index]
            val_next = nums[num_index+1]
            if val_first == val_next:
                nums[num_index] = val_first * 2
                nums[num_index+1] = 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                j+= 1
        
        return nums
            
        