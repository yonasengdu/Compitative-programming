class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for u,v,w in flights:
            graph[u].append((w,v))
            
        heap = [(0,src,k)]
        visited = set()
        cheapest = float("inf")
        
      
        while heap:
            weight,node ,have  = heappop(heap)
            if node == dst:
                cheapest = min(cheapest, weight)
                
            if have < 0:
                continue
            if (node , have)  in visited :
                continue    
                
            
            visited.add((node,have))
            
            for neig_weight,neig_node in graph[node]:
                
                heappush(heap,(neig_weight + weight,neig_node,have - 1))
                
        return cheapest if cheapest != float("inf") else -1
                
            
            
            
    
        
        
        