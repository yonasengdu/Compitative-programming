class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        nums = Counter(deck)
        x = [value for value in nums.values()]
        gcd = x[0]
        
        def GCD(a, b):
            if b == 0:
                return a
            
            return GCD(b, a % b)
        
        for ind in range(1,len(x)):
            gcd = GCD(gcd,x[ind])
        
        if gcd <= 1:
            return False
        # print"
        return True
        
        
        