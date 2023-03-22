class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        high , low = sum(weights),max(weights)
        
        result = high
        
        def isvalid(mid):
            current = mid
            day = 1
            
            for weight in weights:
                if current - weight < 0:
                    current = mid
                    day += 1
                    
                current -= weight
        
            return day <= days
            
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if isvalid(mid):
                result = min(result,mid)
                high = mid - 1
            else:
                low = mid + 1
                
        return result
                
        