class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        ans= [0]*n
        
        def dfs(node,parent):
            counter = Counter(labels[node])
            for child in adj[node]:
                if child == parent: continue
                counter += dfs(child,node)
                
            ans[node] = counter[labels[node]]
            return counter
        
        dfs(0,-1)
        
        return ans
            
        