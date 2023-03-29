class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        checker = set()
        def backtrack(start,comb):
            if len(comb) >= 2:
                if tuple(comb) not in checker:
                    ans.append(comb[:])
                    checker.add(tuple(comb))
               
            
            if len(comb) > len(nums):
                return
            
            for ind in range(start,len(nums)):
                if not comb or comb[-1] <= nums[ind]:
                    comb.append(nums[ind])
                
                    backtrack(ind+1,comb)
                    if comb:
                        comb.pop()
                   
               
                
        backtrack(0,[])
        return ans
            
        