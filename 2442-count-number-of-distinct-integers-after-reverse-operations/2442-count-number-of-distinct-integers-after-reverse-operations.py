class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        set_num = set(nums)
        for ind in nums:
            if ind > 9 or ind < -9:
                str_ind = str(ind)
                set_num.add(int(str_ind[::-1]))
            else:
                set_num.add(ind)
                
        return len(set_num)
                
        