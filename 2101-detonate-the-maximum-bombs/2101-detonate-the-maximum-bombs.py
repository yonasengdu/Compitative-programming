class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.adjecencyList = defaultdict(list)
        n = len(bombs)
        max_detonated = 0
        
        for ind in range(n):
            bomb_1 = bombs[ind]
            x_1 = bomb_1[0]
            y_1 = bomb_1[1]
            r_1 = bomb_1[2]
            
            for nxt in range(n):
                if ind == nxt :
                    continue
                    
                bomb_2 =  bombs[nxt]  
                x_2 = bomb_2[0]
                y_2 = bomb_2[1]
                
                
                
                distance = sqrt(((x_1 - x_2)**2) + ((y_1 - y_2)**2))
                
                if distance <= r_1:
                    self.adjecencyList[ind].append(nxt)
                    
                
                    
              
               
            
    
                    
       
           
        def dfs(node,visited):
          
            
            
             
            for neighbor in self.adjecencyList[node]:
            
                if neighbor not in visited:
                    visited.add(neighbor)
                   
                    dfs(neighbor,visited)
                    
                
                    
                   
                    
          
        
        for node in range(n):
            visited = set([node])
            dfs(node,visited)
            max_detonated = max(max_detonated,len(visited))
           
       
                
        return max_detonated 
                    
                    
        