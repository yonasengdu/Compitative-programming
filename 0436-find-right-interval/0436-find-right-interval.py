class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = []
        needed = [(intervals[i][0],i) for i,_ in enumerate(intervals)]
        
        
        needed.sort(key=lambda x: x[0])
        
        wtf = [i for i,_ in needed]
            
        
        
        for start,end in intervals:
            huh = bisect_left(wtf,end)
            
            if huh >= len(needed):
                result.append(-1)
            else:
                result.append(needed[huh][1])
            
            
        print(result)
        return result
            
            
        
       
        
     
            
            
                
                
            