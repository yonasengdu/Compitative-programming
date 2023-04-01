from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        ans = deque()
        
        for ind in reversed(range(len(nums))):
            temp = bisect_left(s,nums[ind])
            ans.appendleft(temp)
            s.add(nums[ind])
            
        return ans 
        
            
            
        