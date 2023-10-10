class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        
        ans = []
        n = len(A)
        
        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            ans.append(len(setA.intersection(setB)))
            
        return ans
        
        
        
    
        
        
        