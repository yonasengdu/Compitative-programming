class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        newArr = []
        num_pairs = 0
        
        for ind in range(len(nums1)):
            newArr.append(nums1[ind] - nums2[ind])
            
        def merge(left_half,right_half):
            temp = []
            left = 0 
            right = 0
            
            while left < len(left_half)  and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    temp.append(left_half[left])
                    left += 1
                else:
                    temp.append(right_half[right])
                    right += 1

            temp.extend(left_half[left:])
            temp.extend(right_half[right:])

            return temp
        

        def mergeSort(left,right,nums):
            nonlocal num_pairs
            if left == right:
                return [nums[left]]

            mid = left + (right - left)//2
            
            left_half = mergeSort(left,mid,nums)
            right_half = mergeSort(mid + 1,right,nums)
            
          
            for num in right_half:
                num_pairs += bisect_right(left_half,num+diff)
        

            return merge(left_half,right_half)
        
        mergeSort(0,len(newArr) - 1,newArr) 
        
        return num_pairs


            