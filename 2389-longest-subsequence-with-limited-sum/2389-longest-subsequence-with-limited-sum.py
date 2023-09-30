class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for query in queries:
            runSum = 0
            for i in range(len(nums)):
                runSum += nums[i]
                if runSum > query:
                    ans.append(i)
                    break
                    
            if runSum <= query:
                ans.append(i + 1)
                
        return ans
                    
            
            
        