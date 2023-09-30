class Solution:
    def splitNum(self, num: int) -> int:
        nums = sorted(str(num))
        
        groupA = []
        groupB = []
        
        for i in range(len(nums)):
            if i % 2 == 0:
                groupA.append(nums[i])
            else:
                groupB.append(nums[i])
            
        # print(groupA,groupB)
        return int(''.join(groupA)) + int(''.join(groupB))
    
            
            
        
        
        
        
        