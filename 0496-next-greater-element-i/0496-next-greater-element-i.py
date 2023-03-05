class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            tracker = [] 
            flag = False
            for num2 in nums2:
                if tracker and num2 > tracker[-1]:
                    tracker.append(num2)
                    flag = True
                    break
                elif num2 == num1:
                    tracker.append(num2)
            if not flag:
                ans.append(-1)
            else:
                ans.append(tracker[-1])
        return ans