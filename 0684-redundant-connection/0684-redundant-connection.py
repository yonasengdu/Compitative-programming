class UnionFind():
    def __init__(self,size):
        self.root = {i:i for i in range(1, size+1)}
        self.sizes = [1]*(size+1)
        
        
    def find(self,x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    def union(self,x,y):
        repX = self.find(x)
        repY = self.find(y)
        
        if repX != repY:
            if self.sizes[repX] > self.sizes[repY]:
                self.root[repY] = repX
                self.sizes[repX] += self.sizes[repY]
                
            else:
                self.root[repX] = repY
                self.sizes[repY] += self.sizes[repX]
                
    def connected(self ,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = UnionFind(len(edges))
        
        for x, y in edges:
            if not rep.connected(x,y):
                rep.union(x,y)
                
            else:
                return [x,y]
        
        