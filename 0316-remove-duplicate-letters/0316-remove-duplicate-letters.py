# не мое решение
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        visited = set()
       
        last_occurence = { c: i for i, c in enumerate(s) }
    
        for i, c in enumerate(s):
            
            if c not in visited:
              
                while stack and stack[-1] > c and last_occurence[stack[-1]] > i:
                   
                    val = stack.pop()
                    visited.remove(val)
            
                stack.append(c)
                visited.add(c)
 
        return "".join(stack)
        