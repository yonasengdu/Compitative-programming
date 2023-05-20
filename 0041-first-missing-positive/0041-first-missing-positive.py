class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        val = max(nums)
        checker = set(nums)
        
        for i in range(1,val):
            if i not in checker:
                return i
            
        if val < 1:
            return 1
        
        else : return val + 1