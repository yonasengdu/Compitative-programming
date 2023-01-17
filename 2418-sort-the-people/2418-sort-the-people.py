class Solution:
    def sortPeople(self, names: List[str], nums: List[int]) -> List[str]:
        
        for i in range(len(names)):
            min_index = i
            for j in range(i+1,len(names)):
                if nums[min_index] < nums[j]:
                    min_index = j
                    
            nums[i],nums[min_index] = nums[min_index],nums[i]
            names[i], names[min_index] = names[min_index] , names[i]
            
               
        return  names