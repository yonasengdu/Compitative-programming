class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n)
        suffix = [0] * (n)
        
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        
       
        
        for idx in range(1,n):
            prefix[idx] += prefix[idx - 1] + nums[idx]
            suffix[~idx] += suffix[~(idx - 1)] + nums[~idx]
            
      
        
        result = []
        result.append(abs(suffix[1] - (nums[0] * (n - 1))))
                      
    
        
        
        for idx in range(1,n - 1):
            prev = (idx)
            after = (n - prev - 1)
            
            abs_diff = abs(prefix[idx - 1] - (nums[idx] * prev)) + abs(suffix[idx + 1] - (nums[idx] * after))
            result.append(abs_diff)
            
        result.append(abs(prefix[-2] - (nums[-1] * (n - 1))))
            
        return result
            