class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                consequetives = num + 1
                temp = 1
                while consequetives in nums:
                    consequetives += 1
                    temp += 1
                    
                ans = max(ans,temp)
                
                
        return ans
                    
                
    
            
            
                
                
            
            

        