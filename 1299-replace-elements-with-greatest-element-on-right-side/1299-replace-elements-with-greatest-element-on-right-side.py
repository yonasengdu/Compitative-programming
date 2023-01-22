class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        sorted_dict = Counter(sorted((arr),reverse=True))
        for ind in range(len(arr)):
            sorted_dict[arr[ind]] -=1
            if  sorted_dict[arr[ind]] == 0:
                del sorted_dict[arr[ind]]
            if sorted_dict: 
                first_key = next(iter(sorted_dict))
                arr[ind] = first_key
            
        arr[-1] = -1
        return arr
        
            
        
        
      