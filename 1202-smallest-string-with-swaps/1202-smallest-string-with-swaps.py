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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        group_char = defaultdict(list)
        group_i = defaultdict(list)
        
        for x,y in pairs:
            uf.union(x,y)
            
            
        for i in range(len(s)):
            group_i[uf.find(i)].append(i)
            group_char[uf.find(i)].append(s[i])
            
        ans= ['']  * len(s) 
        for g,idx in group_i.items():
            idx.sort()
            char = sorted(group_char[g])
            
            for i,char in zip(idx,char):
                ans[i] = char
                
        return ''.join(ans)
                
            
          
        
            
            
        
            

      
     
        
            
        
            
        
        
  
        

        