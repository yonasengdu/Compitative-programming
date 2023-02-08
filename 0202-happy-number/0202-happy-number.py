class Solution:
    def isHappy(self, n: int) -> bool:
        summ = 0
        prev = set({})
        num = str(n)
        while summ != 1:
            temp = 0
            for i in num:
                temp += int(i)**2
            if temp == 1:
                return True
            elif temp in prev:
                return False
            num = str(temp)
            prev.add(temp)
            

            
        