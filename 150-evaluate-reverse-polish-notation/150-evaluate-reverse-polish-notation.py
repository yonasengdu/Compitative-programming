class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    comp = b + a
                elif i == '-':
                    comp = b - a
                elif i == '*':
                    comp = b*a
                elif i == '/':
                    comp = (b/a)
                    if comp<0:
                        comp = ceil(comp)
                    else:
                        comp = floor(comp)
                stack.append(comp)
            else: 
                val = int(i)
                stack.append(val)
        return stack.pop()
                
        
        
        