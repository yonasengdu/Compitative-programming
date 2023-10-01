class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        n = len(num)
        
        first_min = num[0]
        first_max = num[0]
        
        left = 1
        while left < n and first_max == "9":
            first_max = num[left]
            left += 1
            
        left = 1
        while left < n and first_min == "0":
            first_min = num[left]
            left += 1
            
            
        
        minimum = ''
        maximum = ''
        
        for i in range(n):
            if num[i] == first_max:
                maximum += '9'
                
            else:
                 maximum += num[i]
                
                
            if num[i] == first_min:
                minimum += '0'
                  
            else:
                minimum += num[i]
                
        return int(maximum) - int(minimum)
        