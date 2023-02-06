class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr   = []
        for ind in range(n):
            arr.append(nums[ind])
            arr.append(nums[n+ind])
        return arr