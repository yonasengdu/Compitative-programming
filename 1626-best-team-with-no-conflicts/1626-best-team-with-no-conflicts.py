class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = [(ages[i],scores[i]) for i in range(n)]
        
        pairs.sort()
       
        dp = defaultdict(int)
        
        
        for i in range(n):
            age,score = pairs[i]
            dp[i] = score
            
            for j in range(i):
                p_age, p_score = pairs[j]
                if  score >= p_score  or age  == p_age:
                    dp[i] = max(dp[i],dp[j] + score)
                    
               
         
        
        
        
        return max([val for i,val in dp.items()])
                    
                    
                    
                    
        
        