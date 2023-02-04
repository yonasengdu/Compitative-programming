class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            middle = len(nums1)//2
            median = (nums1[middle] + nums1[middle -1]) / 2
            return median
        else:
            middle =  len(nums1)//2 
            median = nums1[middle]
            return median
            
        