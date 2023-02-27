class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        curr_sum = 0
        len_sub_arr = float("inf")
      
        for right in range(n):   
            curr_sum += nums[right]
            while curr_sum >= target:
                len_sub_arr = min(len_sub_arr,right - left + 1)
                curr_sum -= nums[left]
                left += 1
               

        if len_sub_arr == float("inf"):
            return 0
        return len_sub_arr       
                
                
        
        