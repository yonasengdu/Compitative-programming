class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        flag = False
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                high = mid - 1
                flag = True
                
        first = low if flag else -1
        
        
        low = 0
        high = len(nums) - 1
        flag = False
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                flag = True
                
                
        second = high if flag else -1
        
        return [first,second]
        
        