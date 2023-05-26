class UnionFind():
    def __init__(self,size) -> None:
        self.root = {i:i for i in range(size)}
        self.sizes = [1 for _ in range(size)]

    def find(self, x):
        if self.root[x]  != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        repX = self.find(x)
        repY = self.find(y)

        if repX != repY:
            if self.sizes[repX] > self.sizes[repY]:
                self.root[repY]  = repX
                self.sizes[repX] += self.sizes[repY]
            else:
                self.root[repX]  = repY
                self.sizes[repY] += self.sizes[repX]


    def connected(self,x,y):
        return self.find(x) == self.find(y)
        

    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def get(self):
        return self.root
    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n+1)
        
        for x,y,c in roads:
            uf.union(x,y)
            
            
        roads.sort(key=lambda x:x[2])
        
        for x,y,c in roads:
            if uf.connected(x,n):
                return c
            
            
        
        
        
        
 
        
                
                
            
        
        