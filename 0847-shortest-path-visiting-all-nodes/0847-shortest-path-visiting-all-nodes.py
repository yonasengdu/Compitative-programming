class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        
        def bfs(node):
           
          
            N = len(graph)
            target = ( 2 ** N) - 1
            
            visited = set()
            queue = deque()
            
            queue.append((node,0,0))
            visited.add((node,0))
            
            
            while queue:
             
                curr_node,curr_mask,curr_level = queue.popleft()
                
              
                if curr_mask == target:
                    return curr_level
                    
               
                new_mask = ( 1 << curr_node | curr_mask)
              
                for neigh in graph[curr_node]:
                    if (neigh,new_mask) not in visited:
                        visited.add((neigh,new_mask))
                        queue.append((neigh,new_mask,curr_level + 1))
                        
                        
            return 1
                        
                
                        
        path = float("inf")                
        for i in range(len(graph)):
            path = min(path,bfs(i))
            
        return path - 1
            
                        
                
                        
                
                
            
            
            