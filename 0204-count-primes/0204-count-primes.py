class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * (n)
        is_prime[0] = is_prime[1] = False
        
        d = 2
        while d * d < n:
            if is_prime[d]:
                clear =  d * d
            while clear < n:
                
                is_prime[clear] = False
                
                clear += d
                
            d += 1
        return is_prime.count(True) 