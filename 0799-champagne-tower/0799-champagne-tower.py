class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        def dp(arr,row):
            if row == query_row:
                
                return arr[query_glass]
            
            new_arr = [0]*(len(arr) + 1)
            
              
            for ind in range(len(arr)):
                over_flow = arr[ind] - 1
                if over_flow > 0:  
                    to_next = (over_flow / 2)
                    new_arr[ind] += (to_next)
                    new_arr[ind + 1] += (to_next)
                    
          
            return dp(new_arr,row + 1)
            
            
        ans = dp([poured],0) 
        
        if ans < 1:
            return ans
        else:
            return 1
                
            
            
            
        