class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        Gap_count = defaultdict(int)
        Gap_count[0] = 0
        
        total = len(wall)
        for widths in wall:
            idx = 0
            
            for width in widths[:-1]:
                idx += width
                Gap_count[idx] += 1
         
            
      
        return total - max(Gap_count.values())