class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index = {}
        for index in range(len(nums)):
            num_index[nums[index]] = index
        for old,new in operations:
            index = num_index[old]
            nums[index] = new
            num_index[new] = num_index[old]
        return nums
            
        
             
        
        