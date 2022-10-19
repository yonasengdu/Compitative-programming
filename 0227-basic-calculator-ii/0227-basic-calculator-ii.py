class Solution:
    def calculate(self,k: str) -> int:
            s = []
            stack = []
            for i in range(len(k)):
                if k[i] != " ":
                    if k[i] in "+-*/":
                        if len(stack) >1:
                            num = ""
                            for l in stack:
                                num+=l
                            while stack:
                                stack.pop()
                            s.append(num)
                        else:
                            s.append(stack.pop())  
                        s.append(k[i])         
                    else:
                        stack.append(k[i])
            num = ""
            for l in stack:
                num+=l
            s.append(num)
            ehp =[]
            shift = 0
            i = 0
            while (shift +i) < len(s):
                if s[i+shift] == "/" or s[i+shift] =="*":
                    n = int(ehp.pop())
                    if s[i+shift] == "/":
                        ehp.append(n//int(s[i+shift+1]))
                        shift+=1
                    elif s[i+shift] == "*":
                        ehp.append(n*int(s[i+shift+1]))
                        shift+=1  
                else: 
                    ehp.append(s[i+shift])
                i+=1      
            elp =int(ehp[0])
            for i in range(1,len(ehp)-1,2):
                if ehp[i] == "+":
                    elp+= int(ehp[i+1])
                else:
                    elp-= int(ehp[i+1])

            return elp