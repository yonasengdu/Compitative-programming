class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ctr = 0
        for pointer1,pointer2 in enumerate(reversed(range(len(citations)))):
                    if citations[pointer2]>=pointer1+1:
                        ctr+=1
                    else: break
        return ctr
                          
            
        