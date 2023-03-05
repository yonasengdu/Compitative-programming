class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            current = prices[i]
            is_there_discount = False
            for j in range(i+1,len(prices)):
                if prices[j] <= current:
                    price_after_discount = current - prices[j]
                    ans.append(price_after_discount)
                    is_there_discount = True
                    break
            if not is_there_discount:
                ans.append(current)
        return ans
                
                
        