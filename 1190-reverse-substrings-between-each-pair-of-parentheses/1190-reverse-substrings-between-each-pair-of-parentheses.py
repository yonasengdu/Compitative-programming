class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ref = ""
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                ref = ""
                while stack[-1]!= "(":
                    ref += stack.pop()
                stack.pop()
                for i in ref:
                    stack.append(i)
        return "".join(stack)
        