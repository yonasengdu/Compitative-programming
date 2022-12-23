class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        zero_pointer = len(nums1)-1
        nums1_pointer = m - 1
        nums2_pointer = n - 1
        
        
        
        while  nums1_pointer>=0 and nums2_pointer>=0:
            nums1_element = nums1[nums1_pointer]
            nums2_element = nums2[nums2_pointer]
            element_zero = nums1[zero_pointer]
           
            if nums1_element > nums2_element:
                nums1[nums1_pointer],nums1[zero_pointer] = nums1[zero_pointer],nums1[nums1_pointer]
                zero_pointer -= 1
                nums1_pointer -= 1
                
                
            elif nums2_element >= nums1_element:
                nums1[zero_pointer] = nums2[nums2_pointer]
                zero_pointer -= 1
                nums2_pointer -= 1
          
        if  nums1_pointer < 0:
            while nums2_pointer >= 0:
                nums1[zero_pointer] = nums2[nums2_pointer]
                nums2_pointer -=1
                zero_pointer -= 1
                
                
                
        return nums1
           
                
                
                
       
       


  




    