class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        big = max(x,y)
        small = min(x,y)
        hamming_distance = 0

        while big > 0:
            if big & 1 != small & 1:
                hamming_distance += 1
            big >>= 1
            small >>= 1
            
        return hamming_distance