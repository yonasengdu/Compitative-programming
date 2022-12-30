class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_of_even = 0
        next_pointer = queries[0][1]
        ans = []
        for num in nums:
            if num % 2 == 0:
                sum_of_even += num
                
        for i in range(len(queries)):
            if nums[next_pointer] % 2 == 0:
                sum_of_even -= nums[next_pointer]
                
                
            index = queries[i][1]
            val = queries[i][0]
            nums[index] = nums[index] + val
            if nums[index] % 2 == 0:
                sum_of_even += nums[index]
            ans.append(sum_of_even)
            if i < len(queries)-1:
                next_pointer = queries[i+1][1]
        return ans
          
        