class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = Counter(nums)
        count = 0
        for num in nums:
            if k - num == num:
                count+= num_count[k-num] // 2
                del num_count[k-num]
            elif num_count[k-num] > 0 and num_count[num] > 0:
                count += min(num_count[k-num],num_count[num])
                del num_count[k-num]
                del num_count[num]
                
                
        return count