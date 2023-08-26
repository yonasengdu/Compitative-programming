class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pair = sorted(pairs,key=lambda x : x[1])
        print(pair)
         
        count = 0
      
        for start_idx in range(len(pair)):
            prev = pair[start_idx]
            curr = 1
            for i in range(start_idx + 1,len(pairs)):
                if prev[1] >= pair[i][0]:
                    continue
                    
                curr += 1
                prev = pair[i]
                    
            count = max(count,curr) 
            
            
        return count
                
            
        