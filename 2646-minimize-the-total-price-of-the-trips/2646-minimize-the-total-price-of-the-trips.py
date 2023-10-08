class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        
        
        freq = [0]*n
        
     
        def bfs(start,end):
        
            queue = deque()
            visited = set()
            queue.append((start,[start]))
            
            while queue:
                node,path = queue.popleft()
                 
                if node == end:
                    return path    
                    
                visited.add(node) 
                for neigh in graph[node]:
                    if neigh not in visited:
                        queue.append((neigh,path + [neigh]))
                        
        for start,end in trips:
            path = bfs(start,end)
            
            for node in path:
                freq[node] += 1
                        
        
        
        def dp(node,par,should_half):
            
            if (node,par,should_half) in memo:
                return memo[(node,par,should_half)]
            
            if should_half:
                cost = freq[node]*(price[node]//2)
                
            else:
                cost = freq[node]*(price[node])
                
         
            for neigh in graph[node]:
                if neigh != par:
                    if should_half :
                        neigh_cost = dp(neigh,node,False)
                        
                    else: 
                        neigh_cost = min(dp(neigh,node,False),dp(neigh,node,True))
                        
                    cost += neigh_cost
                    
                    memo[(node,par,should_half)] = cost
                    
            return cost
        
        
        
        cost = float("inf")
        
        memo = {}
        for node in range(n):
            cost = min(cost,dp(node,-1,True),dp(node,-1,False))
            
            
        return cost
            
                        
                    
            
            
        
    