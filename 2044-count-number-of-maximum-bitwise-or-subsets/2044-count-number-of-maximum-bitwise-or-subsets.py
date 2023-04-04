class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.theOr = nums[0]
        self.ans = 0
        for ind in range(1,len(nums)):
            self.theOr |= nums[ind]
        
        def backtrack(start,comb,k):
            if len(comb) == k:
                temp = comb[0]
                for ind in range(len(comb)):
                    temp |= comb[ind]
                
                if temp == self.theOr:
                    self.ans += 1
                    
                return
            
            if start == len(nums):
                return
            
            for ind in range(start,len(nums)):
                comb.append(nums[ind])
                
                backtrack(ind+1,comb,k)
                
                comb.pop()
                
        for k in range(1,len(nums)+1): 
            backtrack(0,[],k)
            
        return self.ans
                
                
                
                
                
                    
            
                    