class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        parentheses_tracker = [0]
       
        
        #
        for pointer in range(len(s)):
            if s[pointer] == "(":
                parentheses_tracker.append(0)
            else:
                current_score = parentheses_tracker.pop()
                parentheses_tracker[-1] += max(2*current_score,1)
                
        return parentheses_tracker[-1]
            
                
                    
                
                
        