class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = float('inf')
        
        while low <= high:
            mid = low + (high - low) // 2
            running_sum = 0
    
            for ind in range(len(nums)):
                temp = ceil(nums[ind] / mid)
                running_sum += temp
            if running_sum > threshold:
                low = mid + 1
            elif running_sum <= threshold:
                high = mid - 1
                ans = min(mid,ans)
            
        return ans
                
                
                
