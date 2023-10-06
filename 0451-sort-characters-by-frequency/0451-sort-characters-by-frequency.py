class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []
        
        for char, count in count.items():
            heappush(heap,(-count,char))
            
        ans = []
        while heap:
            rep,char = heappop(heap)
            
            for _ in range(abs(rep)):
                ans.append(char)
                
                
        return ''.join(ans)
        
        