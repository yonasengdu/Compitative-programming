class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        refactored_tasks = []
        ans = []
        for ind in range(len(tasks)):
            refactored_tasks.append((tasks[ind][0],tasks[ind][1],ind))
            
        
        sorted_tasks =   sorted(refactored_tasks)
        next_task = []
        curr_time = 0
        task_index = 0
        
        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                curr_time = sorted_tasks[task_index][0]
                
            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                _,pt,idx = sorted_tasks[task_index]
                heappush(next_task,(pt,idx))
                task_index += 1
            
            pt, idx  = heappop(next_task)
            curr_time += pt
            ans.append(idx)
            
        return ans
                
            
   