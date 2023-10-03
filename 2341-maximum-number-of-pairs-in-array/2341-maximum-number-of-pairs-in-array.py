class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        formed = 0
        leftOver = 0
        
        for v in count.values():
            leftOver += v % 2
            formed += (v - v % 2) // 2
            
        return [formed, leftOver]
        