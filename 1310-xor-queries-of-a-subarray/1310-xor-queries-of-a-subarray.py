class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = [0]
        length = len(arr) 
        
        computed_xor = []
        
        #pre compute xor
        for ind in range(length):
            pre_xor.append(pre_xor[-1] ^ arr[ind])
            
     
            
            
            
        #compute xor based on quires
        for intervals in queries:
            left = intervals[0]
            right = intervals[1]
            
            temp = pre_xor[right + 1] ^ pre_xor[left]
            computed_xor.append(temp)
                
        return computed_xor
                
            
        
        
        
            
            
            
        
        
        
        
        
        
"""
[1,3,4,8]

[1,1^3,1^3^4,1^3^4^8]


[[0,1],[1,2],[0,3],[3,3]]

1^3^4 = k
1^k = 3^4

X ^ Y = Z

Z ^ x = y

Z ^Y = X
""" 





