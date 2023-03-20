class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
 #        2 -1 2 -3 4 -2 2 
 # prefix 2  1 3  0 4  2 4
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        
        ans = inf
        que = deque()
        que.append([prefix[-1], len(prefix)-1])
        
        for ptr in range(len(prefix)-1, 0, -1):
            while que and que[0][0] < prefix[ptr]:
                que.popleft()
            
            que.appendleft([prefix[ptr], ptr])
            
            while que and que[-1][0] - prefix[ptr-1] >= k:
                ans = min(ans, que[-1][1] - ptr + 1)
                que.pop()
         
        if ans == inf:
            return -1
        return ans