class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numgoodpair = 0
        tracker= {}
        for i in nums:
            if i not in tracker:
                tracker[i]=1
            else:
                tracker[i]+=1
        for i,j in tracker.items():
            numgoodpair += j*(j-1)//2
        return numgoodpair
            
            
       
            
        