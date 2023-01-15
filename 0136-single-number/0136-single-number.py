class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictt = Counter(nums)
        for key,value in dictt.items():
            if value == 1:
                return key
        