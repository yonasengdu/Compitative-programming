class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections = defaultdict(list)
        ans = 0
        for fromm , to in roads:
            connections[fromm].append(to)
            connections[to].append(fromm)
            
        for fromm in range(n):
            for to in range(fromm + 1,n):
                temp = len(connections[fromm]) + len(connections[to]) 
                if [fromm,to] in roads or [to,fromm] in roads:
                    temp -= 1
                ans = max(temp,ans)
        
        return ans
        
        
        
        