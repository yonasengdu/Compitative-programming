class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        
        
        def is_valid(cord):
            return (0 <= cord[0] < len(mat)) and (0 <= cord[1] < len(mat[0]))
        
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row,col))
                    
                    visited.add((row,col))
        level = 1            
        while queue:
            size = len(queue)
            
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            
            
            for cord in range(size):
                cord = queue.popleft()
                
                for dr,dc in directions:
                    new_cord =  (cord[0] + dr,cord[1] + dc)
                    
                    if is_valid(new_cord) and new_cord not in visited:
                        
                        queue.append(new_cord)
                        visited.add(new_cord)
                        
                        mat[new_cord[0]][new_cord[1]] = level
                        
                        
                        
            level += 1
                 
                
        return mat
            
            
            
                
                
                
                
                
            
                
      
                  

                   