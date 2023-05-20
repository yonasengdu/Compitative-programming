class UnionFind():
    def __init__(self) -> None:
        self.root = {}

    def find(self, x):
        if self.root[x]  != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        self.root.setdefault(x,x)
        self.root.setdefault(y,y)
        
        repX = self.find(x)
        repY = self.find(y)
        
        self.root[repY] = repX
  
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = UnionFind()
        for x, y in stones:
            rep.union(x,~y)
            
        return len(stones) - len({rep.find(x) for x in rep.root})
        
