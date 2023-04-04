class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        factorization = set()
            
        for ind in range(len(nums)):
            n = nums[ind]
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d

                d += 1
            if n > 1:
                factorization.add(n)

           
        return len(factorization)
