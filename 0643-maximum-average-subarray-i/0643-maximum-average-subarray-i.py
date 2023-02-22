class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start  = 0
        end = 0
        currSum = 0
        for ind in range(k):
            currSum += nums[end]
            end += 1
        maxAvg = currSum / k
        while end < len(nums):
            currSum -= nums[start]
            currSum  += nums[end]
            start += 1
            end += 1
            maxAvg = max(maxAvg,currSum / k)
        return maxAvg
            
            
        