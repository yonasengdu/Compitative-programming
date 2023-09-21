class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        
        run_sum = sum(nums)
        window = -1
        left = 0
        n = len(nums)
        for right in range(n):
            run_sum -= nums[right]
            while left <= right and run_sum < x:    
                run_sum += nums[left]
                left += 1
                
                
            if  run_sum == x:
                window = max(window,right - left + 1)
                    
        
        return n - window if window > -1 else -1