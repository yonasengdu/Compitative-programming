class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while stones:
            if len(stones) == 1:
                return stones[0] * -1
            stone_1 = heappop(stones)
            stone_2 = heappop(stones)
            
          
            if stone_1 != stone_2:
                heappush(stones,stone_1 - stone_2)
                
        return 0
                
                
                
            
        