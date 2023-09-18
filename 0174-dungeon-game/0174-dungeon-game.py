class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        if dungeon[-1][-1] > 0:
            dungeon[-1][-1] = 0
        
        row = len(dungeon)
        col = len(dungeon[0])
        for i in range(1,col):
            dungeon[~0][~i] =  min(dungeon[~0][~i] + dungeon[~0][~(i - 1)],0)
            
                        
        for i in range(1,row):
            dungeon[~i][-1] = min(dungeon[~i][-1] +  dungeon[~(i - 1)][-1],0)
          
                    
                    
        for i in range(1,row):
            for j in range(1,col):
                dungeon[~i][~j] = min(dungeon[~i][~j]  + max(dungeon[~(i - 1)][~j],dungeon[~i][~(j - 1)]),0)
                
       
    
    
    
    
        return( abs(dungeon[0][0]) + 1) if dungeon[0][0] < 0 else 1
            
            
  
            
            
            
                
                
            
                
                
        
        
        