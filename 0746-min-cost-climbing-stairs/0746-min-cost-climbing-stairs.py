class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*n
        
        pre = cost[0]
        curr = cost[1]
        
        for i in range(2,n):
            temp = curr
            curr = cost[i] + min(pre,curr)
            pre = temp
            
        return min(pre,curr)