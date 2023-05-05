class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def is_valid(node):
            return (0 <= node[0] < len(maze) ) and (0 <= node[1] < len(maze[0])) and (maze[node[0]][node[1]] != "+")
        
        def is_exit(node):
            return node[0] == 0 or node[0] == len(maze) - 1 or node[1] == 0 or node[1] == len(maze[0]) - 1
        
        queue = deque()
        visited = set()
        
        queue.append(tuple(entrance))
        visited.add(tuple(entrance))
        
        steps = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
                if is_exit(curr) and curr != tuple(entrance):
                    return steps
                
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                
                for dr,dc in directions:
                    new_node = (curr[0] + dr,curr[1] + dc)
                    
                    if is_valid(new_node) and new_node not in visited:
                      
                         queue.append(new_node)
                         visited.add(new_node)
                        
            steps += 1
            
        return -1
            
         
                    
                    
                
            
        
        
        