class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i,node in enumerate(equations):
            eadge1,eadge2 = node
            graph[eadge1].append((eadge2,values[i]))
            graph[eadge2].append((eadge1,1/values[i]))

            
        ans = []  
        for start , end in queries:
            queue = [(start,1)]
            if  start not in graph:
                ans.append(-1)
                continue
                
            visited = set([start])
            found = False
            while queue:
                cur,weight = queue.pop()
                
            
                    
                if cur == end:
                    found =  True
                    ans.append(weight)
                    break
                    
                for neig, neig_weight in graph[cur]:
                    if neig  not in visited:
                        queue.append((neig,neig_weight * weight))
                        visited.add(neig)
                    
                    
            if not found :
                ans.append(-1)
                
                
        return ans
                    
                
            
            
        
        