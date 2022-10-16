class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pointer1 = 0
        for pointer2 in range(len(pushed)):
            stack.append(pushed[pointer2])
            while stack and stack[-1] == popped[pointer1]:
                stack.pop()
                pointer1 += 1
        return pointer1 == len(pushed)
                
                
            
                

