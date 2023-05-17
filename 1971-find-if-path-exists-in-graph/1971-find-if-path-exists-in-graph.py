class UnionFind():
    def __init__(self,size) -> None:
        self.root = {i:i for i in range(size)}
        self.sizes = [1]*size

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
     

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = UnionFind(n)
        
        for x , y in edges:
            rep.union(x,y)
            
        return rep.connected(source,destination)
 



    
        