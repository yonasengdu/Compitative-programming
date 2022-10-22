class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        if count[0]%2:
            return []
        for i in sorted(count):
                if count[i]>count[2*i]:
                    return []
                count[2*i]-= count[i] if i else count[i]//2
                
        return list(count.elements())
            
        
        