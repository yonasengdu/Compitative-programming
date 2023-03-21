class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        list1,list2 = grid
        list2.reverse()
        
       
      
        maximized = float("inf")
        
        for ind in range(1,len(list1)):
            list1[ind] += list1[ind - 1]
            list2[ind] += list2[ind - 1]
            
        list2.reverse()
       
        for ind in range(len(list1)):
            top = list1[-1] - list1[ind]
            bottom = list2[0] - list2[ind]
            
            maximized = min(max(top,bottom),maximized)
            
        return maximized
            
        
        
            