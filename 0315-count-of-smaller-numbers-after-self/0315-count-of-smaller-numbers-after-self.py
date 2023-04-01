class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        self.ans = [0]*len(nums)
        
        for ind, val in enumerate(nums):
            nums[ind] = (val,ind)
        
        
        def merge(first,second):
            left = 0
            right = 0
            
            merged = []
            
            while left < len(first) and right < len(second):
                if first[left][0] <= second[right][0]:
                    merged.append(first[left])
                    left += 1
                else:
                    merged.append(second[right])
                    right += 1
                    
            merged.extend(first[left:])
            merged.extend(second[right:])
            

            right_arr = [val for val,ind in second]
        
            for val,ind in first:
                self.ans[ind] += bisect_left(right_arr,val)
                
                
            
            
            return merged
                    
                    
            
        def mergeSort(start,end,arr):
            mid = (start + end) // 2
            
            if mid == start :
                return [arr[start]]
            
            
            left_half = mergeSort(start,mid,arr)
            right_half = mergeSort(mid,end,arr)
            
            
            
            
            return merge(left_half,right_half)
        
       
        
        mergeSort(0,len(nums),nums)
        
        return self.ans
        
        