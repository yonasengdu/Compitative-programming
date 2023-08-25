from itertools import permutations
class Solution:
    def countArrangement(self, n: int) -> int:
        
        nums = list(range(1,n+1))
        beautifuls = 0
        
        def backtrack(nums,l):
            nonlocal beautifuls
            if l == len(nums):
                beautifuls += 1
                
            for i in range(l,len(nums)):
                
                nums[l],nums[i] = nums[i],nums[l]
                
                if nums[l] % (l + 1) == 0 or (l + 1) % nums[l] == 0:
                    # print(f"start {start} nums[i] {nums[i]} i  {i}")
                    backtrack(nums,l + 1 )
                    
                    
                nums[l],nums[i] = nums[i],nums[l]
                
            return beautifuls
                
        
        
        return backtrack(nums,0)
                    
        