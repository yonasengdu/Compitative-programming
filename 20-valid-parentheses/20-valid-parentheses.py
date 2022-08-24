class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{" :
                stack.append(i)
            elif i in ")]}":
                if i == ")" and len(stack)>0 and stack.pop() == "("   :
                    pass
                elif i == "]" and len(stack)>0 and stack.pop() == "[":
                      pass
                elif i == "}" and len(stack)>0 and stack.pop() == "{" :
                     pass
                else: return False
        return len(stack)==0
                
                    
         
                
                