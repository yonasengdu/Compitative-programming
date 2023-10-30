class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(first,second):
            left = 0
            right = 0
            
            merged = []
            
            while left < len(first) and right < len(second):
                if first[left] <= second[right]:
                    merged.append(first[left])
                    left += 1
                else:
                    merged.append(second[right])
                    right += 1
                    
            merged.extend(first[left:])
            merged.extend(second[right:])
            
            return merged
        
        def MergeSort(start,end):
            mid = (start + end) // 2
         
            
            if start == mid:
                return [nums[start]]
            
            left = MergeSort(start,mid)
            right = MergeSort(mid,end)
          
            
            return merge(left,right)
        
        
        n = len(nums)
        return MergeSort(0,n)