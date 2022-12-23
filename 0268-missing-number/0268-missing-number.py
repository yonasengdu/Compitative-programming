class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        n_nums = len(nums)+1
        for num in range(n_nums):
            if num not in set_nums:
                return num
            
        
            
        