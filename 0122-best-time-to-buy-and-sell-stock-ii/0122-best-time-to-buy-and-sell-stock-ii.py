class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices) - 1):
            profit += prices[i + 1] - prices[i] if prices[i + 1] - prices[i]  > 0 else 0
            
        return profit
        
        