class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num =  list(bin(n))
        for ind in range(len(num) - 1):
            if num[ind] == num[ind + 1]:
                return False
        return True
        