class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        count = 0
        tracker = defaultdict(int)
        
        #adding zero with count one for the edge case
        tracker[0] += 1
        
        #bulid tracker and count the sub arr
        for ind in range(len(nums)):
            running_sum += nums[ind]
            check_sum = running_sum - k
                    
            count += tracker.get(running_sum - k,0)
            tracker[running_sum] = tracker.get(running_sum,0) + 1
                
     
            
            
        return count