class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = deque()
        visited = set()
        visited.add(0)
        
        for child in rooms[0]:
            keys.append(child)
        
        
        
        while keys:
            
            key = keys.pop()
            visited.add(key)
            
            for child in rooms[key]:
                if child not in visited:
                    keys.append(child)
                    
        if len(visited) == len(rooms):
            return True
        
        return False
                
                
        