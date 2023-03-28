class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.length = len(nums)
        self.nums = nums
        def backtrack(candidate,validator):
            if len(candidate) == self.length:
                self.ans.append(candidate[:])
                return 
        
            for next_candidate in self.nums:
                if next_candidate not in validator:
                    
                    candidate.append(next_candidate)
                     
                    validator.add(next_candidate)
                     
                     
                    backtrack(candidate,validator)
                    
                    validator.remove(next_candidate)
                    candidate.remove(next_candidate)
        backtrack([],set())
        return self.ans

