class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        
        for i,e in enumerate(nums):
            if target - e in dict:
                return [dict[target-e],i]
            dict[e]= i
            
            
            