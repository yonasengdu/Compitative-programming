class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans  =[]
        ptr = 1
        for num in nums:
            if num >=0:
                ans.append(num)
                ans.append(None)
        for num in nums:
            if num < 0:
                ans[ptr] = num
                ptr += 2
        return ans
                
        
        