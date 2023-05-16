class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        def is_valid(node):
            return (0 <= node[0] < len(grid)) and (0 <= node[1] < len(grid[0])) and grid[node[0]][node[1]] == 1
        
        def dfs(node):
           
         
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            queue.append(node)
            grid[node[0]][node[1]] = 2
            
            for dr , dc in directions:
                neigh = (node[0] + dr , node[1] + dc)
                
                if is_valid(neigh):
                   
                    dfs(neigh)
                    
        start = None
        
        for row in range(len(grid)):
            found = False
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = (row,col)
                    found = True
                    break
            if found:
                break
          
        queue.append(start)
        dfs(start)
        
        
        
        def is_valid_bfs(node):
            return (0 <= node[0] < len(grid)) and (0 <= node[1] < len(grid[0]))
        
            
        def bfs(queue):
            level = 0
            
            while queue:
                size = len(queue)
                directions = [(0,1),(1,0),(0,-1),(-1,0)]
                
                for _ in range(size):
                    curr = queue.popleft()

                   
                        
                    
                        
                    for dr , dc in directions:
                        neigh = (curr[0] + dr , curr[1] + dc)

           
                        if is_valid_bfs(neigh): 
                            if grid[neigh[0]][neigh[1]] == 1:
                                return level 
                        
                            if grid[neigh[0]][neigh[1]] == 0:
                                queue.append(neigh)
                                
                            grid[neigh[0]][neigh[1]] = 2

                level += 1

                
                
       
        return bfs(queue)
                    
                    
                
                
            
        