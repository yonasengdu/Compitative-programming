class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.ans = []
        def helper(row):
            if row == 0:
                return [1]
            
            nextt = helper(row - 1)
            self.ans.append(nextt)
            newFormed = [1]
            for ind in range(len(nextt)-1):
                newFormed.append(nextt[ind] + nextt[ind + 1])
                
            newFormed.append(1)
            
            return newFormed
        
        helper(numRows)
        return self.ans
            
            
        