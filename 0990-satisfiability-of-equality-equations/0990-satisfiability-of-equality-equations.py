class UnionFind():
    def __init__(self) -> None:
        self.root = {i:i for i in string.ascii_lowercase}
   
    def find(self, x):
        if self.root[x]  != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        repX = self.find(x)
        repY = self.find(y)

        
        self.root[repY]  = repX

    def connected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = UnionFind()
        for equation in equations:
            if equation[1] == "=":
                rep.union(equation[0],equation[3])
                
                
        for equation in equations:
            if (equation[1] == "=" and not rep.connected(equation[0],equation[3])):
                return False
            
            elif (equation[1] == "!" and  rep.connected(equation[0],equation[3])):
                return False
            
        return True
                
                
        