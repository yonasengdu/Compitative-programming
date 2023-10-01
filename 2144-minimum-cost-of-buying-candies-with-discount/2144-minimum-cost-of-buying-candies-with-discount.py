class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        
        total = 0
        
        time = 0
        for i in range(len(cost)):
            if time == 2:
                time = 0
                cost.pop()
                
            else:
                total += cost.pop()
                time += 1
                
        return total 
        
        
        
        