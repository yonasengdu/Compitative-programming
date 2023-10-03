class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first = [i for i,_ in costs]
        diff = [j - i for i,j in costs]
        return sum(first)+ sum(sorted(diff)[:len(costs)//2])
        
        