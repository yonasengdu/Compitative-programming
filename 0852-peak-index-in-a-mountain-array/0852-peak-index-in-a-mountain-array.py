class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        
        while low <= high:
            mid = low + (high - low) // 2
           
            
            if nums[mid] < nums[mid + 1] and nums[mid] > nums[mid - 1]:
                low = mid + 1
                if nums[low] > nums[low + 1] and nums[low] > nums[low - 1]:
                    return low
            elif nums[mid] > nums[mid + 1] and nums[mid] < nums[mid - 1]:
                high = mid - 1
                if nums[high] > nums[high + 1] and nums[high] > nums[high - 1]:
                    return high
            elif nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
        return low
    