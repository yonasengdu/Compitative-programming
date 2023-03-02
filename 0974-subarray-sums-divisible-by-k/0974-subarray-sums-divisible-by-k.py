class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_traker = defaultdict(int)
        length = len(nums)
        num_sub_array = 0
        
        #add 0:1 as initial value in remeinder_traker in order to handle the first divisible number (edge case)
        remainder_traker[0] += 1
        
        #calculate the prifix sum
        for ind in range(1, length):
            nums[ind] += nums[ind - 1]
        
        #calculate the number of sub array
        for ind in range(length):
            remainder = nums[ind] % k
            if remainder in remainder_traker:
                num_sub_array += remainder_traker[remainder]
            remainder_traker[remainder] += 1
      
        return num_sub_array
        
        
        
        
