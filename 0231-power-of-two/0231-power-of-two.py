class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        arr = {2**i for i in range(31)}
        if n in arr:
            return True
        return False