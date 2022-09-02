class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lennum1 = len(nums1)
        lennum2 = len(nums2)
        intersection = []
        if lennum1 >= lennum2:
            for i in nums1:
                if i in nums2:
                    intersection.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    intersection.append(i)
                    nums1.remove(i)
        return intersection