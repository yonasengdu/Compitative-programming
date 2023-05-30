class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        target_patt = []
        for slot in target:
            target_patt.append(int(slot))
         
        visited = set()

        queue = deque([(0,0,0,0)])
        
        directions = [(0,1),(1,1),(2,1),(3,1),(0,-1),(1,-1),(2,-1),(3,-1)]
        
        for patt in deadends:
            rep_patt = []
            for slot in patt:
                rep_patt.append(int(slot))
            visited.add(tuple(rep_patt))
                
        level = 0
        if queue[0] in visited:
            queue = deque([])
        while queue:
            size = len(queue)
      
            for _ in range(size):
                curr = queue.popleft()
                curr = list(curr)
                if tuple(curr) == tuple(target_patt):
                        print(curr, target_patt)
                    
                        return level
                
                for ind , mov in directions:
                    new_patt = curr.copy()

                    if new_patt[ind] == 0 and mov == -1:
                        new_patt[ind] = 9

                    elif new_patt[ind] == 9 and mov == 1:
                        new_patt[ind] = 0

                    else:
                        new_patt[ind] += mov
                        

                    new_patt = tuple(new_patt)

                    if new_patt not in visited:
                        visited.add(new_patt)
                        queue.append(new_patt)
            level += 1
         
                        
            
                    
           
                    
        return -1
                
        
        
        