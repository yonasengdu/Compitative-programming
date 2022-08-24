class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                c =0
                for i in range(len(nums)-1):
                    if nums[i-c] == nums[i+1-c]:
                        nums.remove(nums[i-c])
                        nums.append(101)
                        c+=1
                return len(nums)-c
