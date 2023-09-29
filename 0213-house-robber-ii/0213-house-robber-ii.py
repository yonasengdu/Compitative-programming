class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = nums[:]
        n = len(nums)

        if n > 1:
            dp [1] = max( dp [0], dp [1])

        for i in range(2,len(nums) - 1):
             dp [i] = max( dp [i - 1],  dp [i] +  dp [i - 2])

        if n > 2:       
            nums[2] = max(nums[2], nums[1])
        for i in range(3,len(nums)):
            nums[i] = max(nums[i - 1],nums[i] + nums[i - 2])

       
        return max(dp[-2],nums[-1]) if n > 1 else dp[-1]




    