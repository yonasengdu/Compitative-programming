class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]
    
        combination = 0
  
        def backtrack(cSum):
            nonlocal combination
            if cSum == target:
               
                combination += 1
                return 
            
            if cSum > target:
                return 
            
            
            for num in nums:
                backtrack(cSum + num)
                
            return 
        
        backtrack(0)
            
        return combination
        