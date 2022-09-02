class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        snums = list(set(nums))
        snums.sort()
        if len(snums)>2:
            return snums[-3]
        else:
            return snums[-1]