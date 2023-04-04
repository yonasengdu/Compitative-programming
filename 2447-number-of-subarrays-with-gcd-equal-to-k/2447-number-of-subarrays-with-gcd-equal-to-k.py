class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        sub_arr = 0      
        for ind in range(len(nums)):
            temp_gcd = nums[ind]
            sub = [nums[ind]]
            for j in range(ind,len(nums)):
                temp_gcd = gcd(temp_gcd,nums[j])
               
                if temp_gcd == k:
                    sub_arr += 1
                    
              
                if temp_gcd < k:
                    break
                
        return sub_arr
                
                
        