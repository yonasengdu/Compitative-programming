class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nums = edges[0]
        if nums[0] in edges[1]:
            return  nums[0]
        else:
            return nums[1]
        
        
   