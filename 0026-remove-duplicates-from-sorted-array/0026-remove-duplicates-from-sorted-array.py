class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                c =0
                k = len(nums)
                for i in range(len(nums)-1):
                    if nums[i-c] == nums[i+1-c]:
                        nums.remove(nums[i-c])

                        c+=1
                return k-c
