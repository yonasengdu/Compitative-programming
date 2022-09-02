class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snum1 = set(nums1)
        snum2 = set(nums2)
        return list(snum1.intersection(snum2))
        