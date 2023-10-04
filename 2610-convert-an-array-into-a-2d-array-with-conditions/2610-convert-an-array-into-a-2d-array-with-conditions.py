class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        
        maxRep = max([i for _,i in count.items()])
        ans = [[] for _ in range(maxRep)]
        
       
        for num,rep in count.items():
            for i in range(rep):
                ans[i].append(num)
                
        return ans