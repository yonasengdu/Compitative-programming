class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val,min_val = max(nums),min(nums)
        
        diff = max_val - min_val
        
        if 2*k >= diff : return 0
        return diff - 2*k
        