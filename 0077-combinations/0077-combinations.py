class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []
        n += 1
        ans = set()
        
        def solution(curr):
            stack.append(curr)    
            
            if len(stack) >= k:
                # print(stack)
                ans.add(tuple(stack[-k:]))
                
            if curr == n - 1:
                return
            for i in range(curr,n -1):
                # print(curr)
                solution(i+1 )
                stack.pop()
        solution(1)
        return list(ans)
                
                
        
        