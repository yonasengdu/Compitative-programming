class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.adjececyList = defaultdict(list)
        
        for fromm , to  in dislikes:
            self.adjececyList[fromm].append(to)
            self.adjececyList[to].append(fromm)
        
        
        self.groupmap = {i:None for i in range(1,n+1)}
            
        def dfs(node,g):
            
            if not self.groupmap[node]:
                self.groupmap[node] = g
                
            else: return self.groupmap[node] == g
               
                
            for neghibor in self.adjececyList[node]:
                    if not dfs(neghibor, 2 if g == 1 else 1 ):
                        return False
                        
            return True
        
        for node in self.adjececyList.keys():
            if not self.groupmap[node] and not dfs(node,1):
                return False
            
        return True
                
                
            
            
        
            
                  
                 
                
            
            
           
                
                
            
        