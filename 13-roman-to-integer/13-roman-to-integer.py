class Solution:
    def romanToInt(self, s: str) -> int:
                dic = {"I":1,"V":5 , "X":10, "L":50, "C":100, "D":500, "M":1000}
                number = 0
                for i in range(len(s)):
                    k = s[i]
                    if s[i] == "I" and i<len(s)-1:    
                        if s[i+1]=="V":
                            number+= 4
                            number-=5
                        elif s[i+1]=="X":
                            number+= 9
                            number-=10
                        else:
                             number+=1
                    elif s[i]=="X" and  i+1<len(s):
                        if s[i+1]=="L":
                            number+= 40
                            number-=50
                        elif s[i+1]=="C":
                            number+= 90
                            number-=100
                        else: 
                             number += 10
                    elif s[i]=="C" and  i+1<len(s):
                        if s[i+1]=="D":
                            number += 400
                            number-=500
                        elif s[i+1]=="M":
                            number+= 900
                            number-=1000
                        else:
                            number += 100
                    else: 
                        number += dic[k]
                return number