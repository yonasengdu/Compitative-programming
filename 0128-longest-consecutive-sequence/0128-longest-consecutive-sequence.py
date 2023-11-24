class UF():
    def __init__(self,nums):
        self.graph = {par:par for par in nums}
        
        
        
    def find(self,x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])
            
        return self.graph[x]
    
    def union(self,x,y):
        repX = self.find(x)
        repY = self.find(y)
        
        self.graph[repX] = repY
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UF(nums)
        nums = Counter(nums)
        
        
        
        for num,count in nums.items():
            if  num + 1 in nums:
                uf.union(num,num + 1)
                
                
            if num - 1 in nums:
                uf.union(num, num - 1)
                
        for num in nums:
            uf.find(num)
                
        
        ss_length = defaultdict(int)
        ss_length[0] = 0
        
        for ID in uf.graph.values():
                ss_length[ID] += 1
                
        return max(ss_length.values())
                
        
                
        
        
      