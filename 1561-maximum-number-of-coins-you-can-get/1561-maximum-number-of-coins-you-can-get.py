class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 1
        max_coins = 0
        while left < right:
            temp_coins = []
           
            temp_coins.append(piles[left])
            temp_coins.append(piles[right])
            temp_coins.append(piles[right-1])
            max_coins += temp_coins[2]
            left += 1
            right -= 2
        return max_coins