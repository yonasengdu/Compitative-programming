class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        running_sum = 0
        count = 0
        tracker = defaultdict(int)
        
        num = []
        for i in nums:
            if i % 2 == 0:
                num.append(0)
            else:
                num.append(1)
    
        #adding zero with count one for the edge case
        tracker[0] += 1
        
        #bulid tracker and count the sub arr
        for ind in range(len(num)):
            running_sum += num[ind]
         
            count += tracker.get(running_sum - k,0)
            tracker[running_sum] = tracker.get(running_sum,0) + 1
                
     
            
            
        return count
                
        