class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph  = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
      
        
        for ind in range(len(edges)):
            graph[edges[ind][0]].append(edges[ind][1])
        
        
        def bfs(node):
            queue =  deque([node])
            visited = set([node])
            while queue:
                curr = queue.popleft()
                
                for neigh in graph[curr]:
                    if neigh not in visited:
                        ans[neigh].append(node)
                        visited.add(neigh)
                        queue.append(neigh)
                    
                    
                    
        for node in range(n):
            bfs(node)
            
     
        return ans
            
        
    
      
        