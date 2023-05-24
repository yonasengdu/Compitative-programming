class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        summ = 0
        for i in range(k):
            if numOnes: 
                summ += 1
                numOnes -= 1
            elif numZeros:
                numZeros -= 1
                
            elif numNegOnes:
                numNegOnes -= 1
                summ -= 1
                    
        return summ
                
                
        