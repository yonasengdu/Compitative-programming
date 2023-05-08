class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = []
        ans = []
        for word,count in Counter(words).items():
            word_count.append((-count,word))
            
        heapify(word_count)
        
        for _ in range(k):
            ans.append(heappop(word_count)[1])
            
        
        return ans
    