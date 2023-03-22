class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low ,high = 1,max(piles)
        
        result = high
        
        def canEat(mid):
            hours = 0
            speed = mid
          
            for pile in piles:
                hours += ceil(pile / speed)
                
       
                
            return hours <= h
                
                 
        
        while low <= high:
            
            mid =  low + (high - low)//2
            
            if canEat(mid):
                result = min(result,mid)
                high = mid - 1
                
            else:
                low = mid + 1
                
        return result
        