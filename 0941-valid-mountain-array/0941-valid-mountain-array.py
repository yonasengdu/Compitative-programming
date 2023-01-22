class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_ind = arr.index(max(arr))
        
        flag = False
        for i in range(1,max_ind):
            if arr[i-1]>=arr[i]:
                return False
         
        if arr[:max_ind] and arr[max_ind+1:]:
            flag = True
            print("passed")
            
        for i in range(max_ind+1, len(arr)):
            if arr[i-1] <= arr[i]:
                return False
            
       
            
        if flag:
            return True 
        else:
            return False
        
     
        