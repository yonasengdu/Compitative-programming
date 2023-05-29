class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findTargetSumWays(idx , tally,memo = defaultdict(tuple)):
            if idx == len(nums) and tally == target:
                return 1
            if idx == len(nums):
                return 0
            
            if (idx , tally) in memo:
                return memo[(idx,tally)]
            
            memo[(idx,tally)] = findTargetSumWays(idx+1 , tally + nums[idx]) + findTargetSumWays(idx+1,tally - nums[idx])
            
            return memo[(idx,tally)]
        
        return findTargetSumWays(0,0)
        