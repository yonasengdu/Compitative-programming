class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend / divisor
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        elif a>0:
            return floor(a)
        return ceil(a)