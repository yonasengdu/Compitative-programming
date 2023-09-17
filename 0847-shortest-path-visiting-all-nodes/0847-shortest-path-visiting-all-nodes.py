class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))
        
        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))
        
        
#         def bfs(node):
           
          
#             N = len(graph)
#             target = ( 2 ** N) - 1
            
#             visited = set()
#             queue = deque()
            
#             queue.append((node,0,0))
#             visited.add((node,0))
            
            
#             while queue:
             
#                 curr_node,curr_mask,curr_level = queue.popleft()
                
              
#                 if curr_mask == target:
#                     return curr_level
                    
               
#                 new_mask = ( 1 << curr_node | curr_mask)
              
#                 for neigh in graph[curr_node]:
#                     if (neigh,new_mask) not in visited:
#                         visited.add((neigh,new_mask))
#                         queue.append((neigh,new_mask,curr_level + 1))
                        
                        
#             return 1
                        
                
                        
#         path = float("inf")                
#         for i in range(len(graph)):
#             path = min(path,bfs(i))
            
#         return path - 1
            
                        
                
                        
                
                
            
            
            