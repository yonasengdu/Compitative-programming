class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
     
        @cache
        def backtrack(cSum):
          
            if cSum == target:
               
              
                return 1
            
            if cSum > target:
                return 0
            
            
            count = 0
            for num in nums:
                count += backtrack(cSum + num)
                
            return count
        
        return backtrack(0)
            
      
        