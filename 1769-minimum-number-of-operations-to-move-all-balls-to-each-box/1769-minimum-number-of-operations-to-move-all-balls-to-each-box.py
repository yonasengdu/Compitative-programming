class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        
        for i in range(len(boxes)):
            temp_count = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                if boxes[j] == "1":
                    temp_count += abs(j-i)
            ans.append(temp_count)
        return ans
                    
                    
                
        
        