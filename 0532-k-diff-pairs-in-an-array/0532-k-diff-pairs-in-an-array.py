class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = Counter(nums)
        cross_check = set()
        unique_pairs = 0
        if k == 0:
            for rep in count.values():
                unique_pairs += 1 if rep >= 2 else 0
                
            return unique_pairs
        
        for num in nums:
            
            if num - k in count and (num, num-k) not  in cross_check:
                cross_check.add((num,num-k))
                cross_check.add((num-k,num))
                unique_pairs += 1
                
            if  num + k in count and (num,num+k) not in cross_check:
                
                cross_check.add((num,num+k))
                cross_check.add((num+k,num))
                unique_pairs += 1
                
          
      
        return unique_pairs
    
    
                
                