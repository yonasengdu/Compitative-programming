class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextGreater = [-1] * len(nums)
        l = len(nums)
        nums += nums
        stack = []
        for idx, num in enumerate(nums):
            while stack and num > stack[-1][1]:
                i, v = stack.pop()
                nextGreater[i % l] = num
            stack.append([idx, num])
        return nextGreater
