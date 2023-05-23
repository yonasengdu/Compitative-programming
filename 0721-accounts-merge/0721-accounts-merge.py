class UnionFind():
    def __init__(self) -> None:
        self.root = {}
 

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        parents = defaultdict(set)
        name = {}
        
        ans = []
        for group in accounts:
            for email in group[1:]:
                uf.root[email] = email
                
                
        for group in accounts:
            common = group[1]
            name[common] = group[0]
            
            for i in range(2,len(group)):
                uf.union(common,group[i])
                
        for group in accounts:
            for email in group[1:]:
                parents[uf.find(email)].add(email)
                
                
        for par, emails in parents.items():
            emails = list(emails)
            emails.append(name[par])
            emails[0],emails[-1] = emails[-1],emails[0]
            
            emails[1:] = sorted(emails[1:])
            ans.append(emails)
            
        return ans
     
                
                
                
     
                
        
                
                
     
            
           

        
