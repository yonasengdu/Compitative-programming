# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        
        low = 0
        high = mountain_arr.length() - 1
        n = high
        peak = -1
        
        while low <= high:
            
            mid = (low + high)//2
            mid_val = mountain_arr.get(mid)
            mid_left = float("-inf")
            mid_right = float("inf")
            
            if mid - 1 >= 0:
                mid_left = mountain_arr.get(mid - 1)
                
            if mid + 1 <= n:
                mid_right = mountain_arr.get(mid + 1)


            if mid_left < mid_val < mid_right:
                    low = mid + 1

            elif mid_left > mid_val > mid_right:
                    high = mid - 1

            elif mid_left < mid_val > mid_right:
                peak = mid
                break
                    
        
                

      
        print(peak)
        
        low = 0
        high = peak 

        finding1 = float('inf')

        while low <= high:

            mid = (low + high)//2

            mid_val = mountain_arr.get(mid)
           

            if mid_val < target:
                low = mid + 1

            elif mid_val > target:
                high = mid - 1

            elif mid_val == target:
                finding1 = mid
                break
                
            else:
                break

                
                
                

        low = peak
        high = mountain_arr.length() - 1
        finding2 = float('inf')
        
        while low <= high:

            mid = (low + high)//2

            mid_val = mountain_arr.get(mid)

           
    
            if mid_val > target:
                low = mid + 1

            elif mid_val < target:
                high = mid - 1

            elif mid_val == target:
                
                finding2 = mid
                break
          
                

        ans = min(finding1,finding2) 
        
        return ans if ans != float('inf') else -1

                
                
                
            


 
        