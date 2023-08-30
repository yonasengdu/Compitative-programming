class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        
        
        
        if source == target:
            return 0
        
        queue = deque()
        visited = set()
        for i,route in enumerate(routes):
            for r in route:
                if r == source:
                    queue.append(i)
                    visited.add(i)
                    
                
                graph[r].add(i)
                
                
        level = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                for sta in routes[curr]:
                    if sta == target:
                        return level
                    
                    for bus in graph[sta]:
                        if bus not in visited:
                            visited.add(bus)
                            queue.append(bus)
                            
            level += 1
            
        return -1
                
            
                
                
        
     
                        
                        
            
            