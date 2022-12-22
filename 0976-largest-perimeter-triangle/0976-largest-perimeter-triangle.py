class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            temp_tri = nums[i:i+3]
            if temp_tri[0]+ temp_tri[1] <=  temp_tri[2]:
                continue
            elif temp_tri[1]+ temp_tri[2] <= temp_tri[0]:
                continue
            elif temp_tri[0]+ temp_tri[2] <=  temp_tri[1]:
                continue
            else:
                return temp_tri[0]+ temp_tri[1] + temp_tri[2]
        return 0
        