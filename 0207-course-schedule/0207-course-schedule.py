class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses) ] 
        
        for take,pre in prerequisites:
            courses[pre].append(take)
            colors[take] += 1
            
            
        ans = []    
        queue = deque()
        
        for ind,node in enumerate(colors):
            if not node:
                queue.append(ind)
            

                
        while queue:
            curr = queue.popleft()
          
            
            ans.append(curr)
            
            for child in courses[curr]:
                colors[child] -= 1
                if colors[child] == 0:
                    queue.append(child)
                    
             
        if len(ans) != numCourses:
            return False
        return True
            
            
            
                