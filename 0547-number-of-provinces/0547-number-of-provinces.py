class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjecency_list = defaultdict(list)
        
        def dfs(node,visited):
            if not adjecency_list:
                return 
            
            for neighbor in adjecency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor,visited)
                
        for ind ,row in enumerate(isConnected):
            for val,col in enumerate(row):
                if col == 1:
                    adjecency_list[ind].append(val)
                
                
                
        provinces  = 0
        visited = set()
        for start in adjecency_list.keys():
            if start not in visited:
                provinces += 1
                visited.add(start)
                dfs(start,visited)
                
        return provinces
                
                
        
        