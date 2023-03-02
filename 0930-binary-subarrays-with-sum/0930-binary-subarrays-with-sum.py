class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum = 0
        hash_map = defaultdict(int)
        hash_map[0] = 1
        count = 0
        
        #
        for ind in range(len(nums)):
            running_sum += nums[ind]
            count += hash_map.get(running_sum - goal, 0)
            hash_map[running_sum] += 1
        
        return count
            
            
            
            
            