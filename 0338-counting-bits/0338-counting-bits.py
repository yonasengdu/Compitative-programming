class Solution:
    def countBits(self, n: int) -> List[int]:
        memory = dict()
        memory[0] = 0
        
        result = []
        
        for val in range(n+1):
            count = 0
            if val & 1 == 1:
                count += 1
                
            nxt = val >> 1
            count += memory[nxt]
            memory[val] = count
            
            result.append(count)
        return result
            