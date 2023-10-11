class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        ans = 0
        n = len(rating)
        
        for j in range(n):
            less_Before = 0
            less_after = 0
            greater_Before = 0
            greater_after = 0
            
            for ptr in range(n):
                
                if ptr < j:
                    if rating[ptr] < rating[j]:
                        less_Before += 1
                        
                    if rating[ptr] > rating[j]:
                        greater_Before += 1
                        
                if ptr > j:
                    if rating[ptr] < rating[j]:
                        less_after += 1
                        
                    if rating[ptr] > rating[j]:
                        greater_after += 1
                        
            ans +=  (less_Before * greater_after) + (greater_Before * less_after)
            
            
            
        return ans
                    

        
        