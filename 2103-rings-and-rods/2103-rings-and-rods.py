class Solution:
    def countPoints(self, rings: str) -> int:
        count = defaultdict(set)
    
        
        for i in range(0,len(rings),2):
            count[rings[i + 1]].add(rings[i])
            
          
        ringsWith3 = 0
        for i,ring in count.items():
            if len(ring) == 3:
                ringsWith3 += 1
                
        return ringsWith3
            
        
            
        