class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        offSet = ord('a') - 1
        hash_right = 0
        left = 0
        s = s[::-1]
        ans = []
        
        powers = [1]
        
        for i in range(1,k+1):
            powers.append((powers[-1]*power)%modulo)
            
        
        
        for right in range(len(s)):
            hash_right = ((hash_right * power) + (ord(s[right]) - offSet)) % modulo
            
            if right - left + 1 == k:
                if hash_right == hashValue:
                    ans.append(''.join(s[left:right+1]))
                
                hash_right -= ((ord(s[left]) - offSet) * powers[k-1])
                hash_right %= modulo
                left += 1
            
            
            
        return ans[-1][::-1]
        
        