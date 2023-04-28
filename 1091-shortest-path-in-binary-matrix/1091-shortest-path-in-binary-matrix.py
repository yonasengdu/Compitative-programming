class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        path = deque()
        visited = set()
        n = len(grid)
        target = (n -1 ,n -1)
        
        def is_valid(x,y):
            return (0 <= x < n) and (0 <= y < n) and (grid[x][y] == 0)
        
        
        if grid[0][0] == 0:
            path.append(((0,0),1))
            visited.add((0,0))
            
            if (0,0) == target:
                return 1
            
        else:
            return -1
        
        while path:
            
            current = path.popleft()
            
            directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
            
            for dx,dy in directions:
                
                new_x = current[0][0] + dx
                new_y = current[0][1] + dy
                level = current[1] + 1
                bundle = (new_x,new_y)
                new_val = (bundle,level)
              
                
             
                
                if is_valid(new_x,new_y) and bundle not in visited:
                    if (bundle) == target:
                        return new_val[1]
                    visited.add((new_x,new_y))
                    path.append(new_val)
                    
                    
        return -1
        
        