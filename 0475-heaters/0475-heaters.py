



class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        
        left = 0
        radius = 0
        
        n = len(houses)
        m = len(heaters)
        
        houses.sort()
        heaters.sort()
        
        for right in range(n): 
            while  left + 1 < m and abs(houses[right] - heaters[left]) >= abs(houses[right] - heaters[left + 1]):
                    left += 1         
                    
            radius = max(radius,abs(houses[right] - heaters[left]))
            
        return radius
                    
                    