class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxx = height[0]
        left = height[:]
        right = height[:]
        
        total_water = 0
        
        for idx in range(len(height)):
            if left[idx] < maxx:
                left[idx] = maxx
                
            else:
                maxx = left[idx]
                
            
        maxx = height[-1]
        for idx in reversed(range(len(height))):
            if right[idx] < maxx:
                right[idx] = maxx
                
            else:
                maxx = right[idx]
                
                
        for idx in range(1,len(height)  - 1):
            curr_water = (min(left[idx - 1],right[idx + 1])) - height[idx]
            
            if curr_water > 0: 
                total_water += curr_water
                
                
        return total_water
            
            
                
         
        
                
        
        