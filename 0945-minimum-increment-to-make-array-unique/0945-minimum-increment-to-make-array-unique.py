class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                result+= nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
        return result