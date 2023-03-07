class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_position = []
        tracker = []
        
        for ind in range(len(position)):
            time_position.append([position[ind],(target - position[ind]) / speed[ind]])
      
        time_position.sort(key=lambda x : x[0],reverse=True  )
        
        
        for position,time in time_position:
            if not tracker:
                tracker.append(time)
            elif tracker[-1] < time:
                tracker.append(time)
        return len(tracker)

       
        
            
            
        
        