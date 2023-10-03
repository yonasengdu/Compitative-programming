class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = [[] for _ in range(n)]
        
        for u , v, w in times:
            graph[u - 1].append((v - 1,w))
            
        visited = [float(inf)]*n
        
        heap = [(0,k-1)]
        
        while heap:
            weight,node = heappop(heap)
            
            if visited[node]  <= weight:
                continue
                
            visited[node] = weight
            
            for neigh,neigh_weight in graph[node]:
                heappush(heap,(neigh_weight + weight,neigh))
                
   
        min_time =  max(visited) 
    
        return min_time if  min_time != float(inf) else -1 
            
        
     