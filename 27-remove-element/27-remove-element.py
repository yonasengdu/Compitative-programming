class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            c = 0
            for i in range(len(nums)):
                    if nums[i-c] == val:
                        nums.remove(nums[i-c])
                        c+=1
            return len(nums)

