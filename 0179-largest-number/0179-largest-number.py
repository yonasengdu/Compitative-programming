class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            for i,n in enumerate(nums):
                nums[i] = str(n)
            def compare(n1,n2):
                if n1 + n2 < n2 + n1:
                    return 1
                elif n1 + n2 == n2 + n1:
                    return 0
                else:
                    return -1
            LargestNumber = sorted(nums,key=cmp_to_key(compare))
            return str(int("".join(LargestNumber)))


