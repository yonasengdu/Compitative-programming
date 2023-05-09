class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNodes = []
        
        
        def findSafe(node):
            if g_colors[node] == "G":
                return False
            
            if g_colors[node] == "B":
                return True
            
            g_colors[node] = "G"
        
            
            for child in graph[node]:
                if g_colors[child] == "B":
                    continue
                
                    
                if not findSafe(child) :
                    return False
                
            g_colors[node] = "B"
            
        
            return True
            
            
        g_colors = ["W" for _ in range(len(graph))]   
        for node in range(len(graph)):

            
            if findSafe(node):
                safeNodes.append(node)
           
                
                
        return safeNodes
            
            
       
        
   
            
            
        