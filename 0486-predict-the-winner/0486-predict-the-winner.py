class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def PredictTheWinner(left,right,score1,score2,turn):
            if left > right:
                return score1 >= score2
            if turn:
                return PredictTheWinner(left + 1,right,score1 + nums[left],score2,not turn) or PredictTheWinner(left,right - 1,score1 + nums[right],score2,not turn)
            
            return  PredictTheWinner(left + 1,right,score1 ,score2 + nums[left],not turn) and PredictTheWinner(left,right - 1,score1 ,score2 + nums[right],not turn)
        
        return PredictTheWinner(0, len(nums) - 1, 0 , 0, True)
            
        