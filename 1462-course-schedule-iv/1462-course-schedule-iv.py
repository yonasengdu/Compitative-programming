class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0]*numCourses
        
        for pre , course in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
            
        queue =  deque()
        
        for node in range(numCourses):
            if incoming[node] == 0:
                queue.append(node)
                
                
        top_sort = [set() for _ in range(numCourses)]
        
        while queue:
            n = len(queue) 
            
            for _ in range(n):
                curr = queue.popleft()
                
                for neig in graph[curr]:
                    
                    incoming[neig] -= 1
                    top_sort[neig].add(curr)
                    top_sort[neig].update(top_sort[curr])
                    
                    
                    if incoming[neig] == 0:
                        queue.append(neig)
                        
        
        ans = []
        
        for u , v in queries:
            if u in top_sort[v]:
                ans.append(True)
                
            else:
                ans.append(False)
                
                
        return ans
                    
                
                
                
            
        
        
    