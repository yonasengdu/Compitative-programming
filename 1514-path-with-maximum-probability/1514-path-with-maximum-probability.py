class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
    
    
        dist = [0]*n
        dist[start_node] = 1
        
        graph = [[] for _ in range(n)]
        
        for i,edge in enumerate(edges):
            fromm, to = edge
            graph[fromm].append((to,succProb[i]))
            graph[to].append((fromm,succProb[i]))
            
        heap = [(-1,start_node)]
        
        while heap:
            weight,node = heappop(heap)
            
            if dist[node] <= weight:
                continue
                
            dist[node] = weight  
            for neig,neig_weight in graph[node]:
                prob = weight * neig_weight
                heappush(heap,(prob,neig))
                    
                    
                    
        
        
                    
                    
        
         
       
        return -1*dist[end_node]
    
    
    
    
    
    
    
    
    
    
    
    
#         dist = [0]*n
#         dist[start_node] = 1
        
#         for  _ in range(n-1):
#             for  i,edge in enumerate(edges):
#                 u,v = edge
#                 if  dist[u] != 0 and dist[u]*succProb[i] > dist[v]:
#                     dist[v] = dist[u]*succProb[i]
                    
#                 if  dist[v] != 0 and dist[v]*succProb[i] > dist[u]:
#                     dist[u] = dist[v]*succProb[i]
                    
                    
        
         
        
#         return dist[end_node]
    