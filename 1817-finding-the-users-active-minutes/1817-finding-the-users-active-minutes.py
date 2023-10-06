class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        pre = defaultdict(set)
        
        for ID,time in logs:
            pre[ID].add(time)
            
            
        
        count = defaultdict(int)
        
        for ID,times in pre.items():
            count[len(times)] += 1
            
            
        ans = []
        for j in range(1,k+1):
            ans.append(count[j])
            
        return ans
        
        
        