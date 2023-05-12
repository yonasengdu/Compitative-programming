class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        num = [(-i,j) for j,i in count.items() ]
        ans = []
        heapify(num)
        for _ in range(k):
            ans.append(heappop(num)[1])
            
        return ans
    