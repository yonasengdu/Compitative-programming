class UnionFind():
    def __init__(self) -> None:
        self.root = {chr(i):chr(i) for i in range(97,123)}
        

    def find(self, x):
        if self.root[x]  != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        repX = self.find(x)
        repY = self.find(y)

        if repX != repY:
            
            if ord(repX) < ord(repY):
                self.root[repY]  = repX
              
            else:
                self.root[repX]  = repY
               


    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def get(self):
        return self.root
    
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = UnionFind()
        
        for ind in range(len(s1)):
            x  = s1[ind]
            y  = s2[ind]
            rep.union(x,y)
            
        ans = []
        root = rep.get()
        
        # print(root)
        for char in baseStr:
            ans.append(rep.find(char))
           
        # print(">> ", ans)

        
        return "".join(ans)
            
            
            
        