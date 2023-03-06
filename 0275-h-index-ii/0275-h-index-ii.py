class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations) - 1
        length = len(citations)
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if citations[mid] >= length - mid:
                high = mid - 1
            else:
                low = mid + 1
        return length - low