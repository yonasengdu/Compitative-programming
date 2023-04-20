class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.target = len(graph) - 1
        
        def dfs(node,path,output):
            if node == self.target:
                output.append(path)
                
                
            for neighbor in graph[node]:
                dfs(neighbor,path + [neighbor],output)
                
                
            return output
        
        return dfs(0,[0],[])
        
        