class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += ''.join([st]*k)
            else:
                stack[-1][0] += ch
        return stack[0][0]
    