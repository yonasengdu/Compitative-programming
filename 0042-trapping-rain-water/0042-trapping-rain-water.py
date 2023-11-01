class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = height[0]
        max_right = height[-1]
        
        left = 0
        right = len(height)  - 1
        
        total = 0
        
        while left < right:
            upper = min(max_left,max_right) 
            limit = min(height[left] , height[right])
            
            temp = upper - limit
            
            if temp > 0:
                total += temp
            
            if max_left <= max_right:
                left += 1
                
                
            else:
                right -= 1
                
                
            max_right = max(max_right,height[right])
            max_left = max(max_left,height[left]) 
                

                
        return total
                
            
        
        