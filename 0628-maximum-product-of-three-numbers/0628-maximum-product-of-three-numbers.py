class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        ans.append(nums[~0]* nums[~1] * nums[~2])
        ans.append(nums[0]* nums[1] * nums[2])
        ans.append(nums[0]* nums[1] * max(nums))
        return max(ans)