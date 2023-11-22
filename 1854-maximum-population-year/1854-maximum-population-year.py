class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        n = (2050 - 1950) + 1
        offSet = 1950
        prefix = [0] * (n)

        for birth,death in logs:
            prefix[birth - offSet] += 1
            prefix[death - offSet] -= 1
            
        
        for i in range(1,n - 1):
            prefix[i] += prefix[i - 1]

        earliest_year = 0
        max_population = 0

        
        for  curr_year,curr_population in enumerate(prefix):
            if curr_population > max_population:
                max_population = curr_population
                earliest_year = curr_year + offSet
        
        

        return earliest_year

