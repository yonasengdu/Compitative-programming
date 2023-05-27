class Solution:
    def tribonacci(self, n: int,memo = defaultdict(int)) -> int:
        if 0 <= n <= 1:
            return n
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        
        memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        
        return memo[n]