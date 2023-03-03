class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
    
        
        end = x
        low = 0
        high = end
        while low <= high:
            mid = low + (high - low) // 2
            if mid**2 < end and (mid + 1)**2 <= end:
                low = mid + 1
            elif mid**2 > end : 
                high = mid - 1
            else: 
                return mid
            
       
        