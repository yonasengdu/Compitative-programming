class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        Heap = [(-cnt,val) for val,cnt in freq.items()]
        heapify(Heap)
        
        ans = []
        for _ in range(k):
            curr = heappop(Heap)
            ans.append(curr[1])
            
        return ans
        
        
              
        