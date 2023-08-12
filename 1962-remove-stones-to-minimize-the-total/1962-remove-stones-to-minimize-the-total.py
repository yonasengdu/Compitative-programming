class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in range(len(piles)):
            heappush(heap,-piles[i])
            
        for i in range(k):
            substracee = heappop(heap)
            diff = floor(abs(substracee)/2)
            heappush(heap,substracee + diff)
            
        return abs(sum(heap))
        