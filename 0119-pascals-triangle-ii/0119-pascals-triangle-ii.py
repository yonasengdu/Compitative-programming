class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if  rowIndex < 2:
            return [1 for _ in range(rowIndex + 1)]
        
        prev = self.getRow(rowIndex - 1)
        
        ans = [1 for _ in range(rowIndex + 1)]
        
        for i in  range(rowIndex-1):
            ans[i + 1] = prev[i] + prev[i + 1]
         
        return ans
        