class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set()
        
        for fromm,to in edges:
            reachable.add(to)
            
        ans = [] 
        for ind in range(n):
            if not ind in reachable:
                ans.append(ind)
                
        return ans
                
                
                
            
            
            
        
        