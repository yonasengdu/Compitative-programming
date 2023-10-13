class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        run_and = nums[0]
        ans = 1
        
        for i in range(1,len(nums)):
            run_and &= nums[i]
            
        if run_and > 0:
            return 1
        
        run_and = 2**32-1
        ans = 0
        for right in range(len(nums)):
                run_and &= nums[right]
                
                if run_and == 0:
                    ans += 1
                    run_and = 2**32-1
                
        
        return ans