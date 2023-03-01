class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        
         # calculate the left product of each number 
        for ind in range(1,n):
                left_product[ind] = left_product[ind - 1] * nums[ind - 1]
                
        # calculate the right product of each number
        for ind in range(1,n):
                right_product[~ind] = right_product[~(ind -1)] * nums[~(ind - 1)]
            
        #calculate the product of array exept it self
        for ind in range(n):
            nums[ind] = left_product[ind] * right_product[ind]
            

        return nums
        
        