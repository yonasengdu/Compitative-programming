class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1)])
        visited = set()
        
        level = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                curr_pos,curr_speed = queue.popleft()
                
                
                if curr_pos == target:
                    return level
                
                if not (curr_pos + curr_speed,curr_speed * 2) in visited:
                    queue.append((curr_pos + curr_speed,curr_speed * 2))
                    visited.add((curr_pos + curr_speed,curr_speed * 2))
                
                if curr_speed > 0:
                    if not (curr_pos,-1) in visited:
                        queue.append((curr_pos,-1))
                        visited.add((curr_pos, -1))
                    
                else: 
                    if not (curr_pos,1) in visited:
                        queue.append((curr_pos,1))
                        visited.add((curr_pos, 1))
                    
            level += 1
                
                
            
            