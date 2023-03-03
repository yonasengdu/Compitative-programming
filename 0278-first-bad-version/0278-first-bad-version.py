# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            if not isBadVersion(mid):
                low = mid + 1
            elif isBadVersion(mid) and isBadVersion(mid - 1):
                high = mid - 1
            else: 
                return mid
            
        
        