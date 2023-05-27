class Solution:
    def fib(self, n: int,memo = defaultdict(int)) -> int:
        if 0<= n <= 1:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.fib(n-1) + self.fib(n-2)
        
        return memo[n]
        