class Solution:
    def closestPrimes(self, left: int, n: int) -> List[int]:
        is_prime: list[bool] = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        i = 2
        while i <= n:
            if is_prime[i]:
                j = 2 * i
            while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1
        is_prime_new = [_ for _ in range(left,len(is_prime)) if is_prime[_] == True]
        
        diff = float("inf")
        ans = [-1,-1]
        
        for ind in range(len(is_prime_new) - 1):
            temp_diff = is_prime_new[ind + 1] - is_prime_new[ind] 
            if temp_diff < diff:
                diff = temp_diff
                ans = [is_prime_new[ind] ,is_prime_new[ind + 1]]
                
        return ans
            
            
            
        
       