class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastInd = len(nums) - 1
        
        for i in range(len(nums) - 2,-1,-1):
            if abs(lastInd - i <= nums[i]):
                lastInd = i
                
        if lastInd == 0:
            return True
        return False