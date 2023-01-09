class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1_arr = num1.split("+")
        nums2_arr = num2.split("+")
        nums1_arr[1] = nums1_arr[1][:-1]
        nums2_arr[1] = nums2_arr[1][:-1]
        ans = []
        for i in nums1_arr:
            for j in nums2_arr:
                temp = int(i) * int(j)
                ans.append(temp)
        return f"{ans[0]-ans[3]}+{ans[1]+ans[2]}i"
        