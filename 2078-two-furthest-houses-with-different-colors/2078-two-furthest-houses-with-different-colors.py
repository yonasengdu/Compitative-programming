class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        theDistance = 0
        n = len(colors)
        
        for first in range(n):
            for nextt in range(first,n):
                if colors[first] != colors[nextt]:
                    theDistance = max(theDistance,nextt - first)
                    
        return theDistance
                
        