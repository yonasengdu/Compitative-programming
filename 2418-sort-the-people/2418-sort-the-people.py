class Solution:
    def sortPeople(self, names: List[str], nums: List[int]) -> List[str]:
        
        for i in range(len(names)):
            for j in range(len(names)-1):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    names[i], names[j] = names[j], names[i]
               
        return  names