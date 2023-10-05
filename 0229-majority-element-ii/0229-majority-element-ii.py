class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        shouldHappen = len(nums) // 3
        
        ans = []
        
        
        
        for num,rep in count.items():
            if rep > shouldHappen:
                ans.append(num)
                
        return ans 
        