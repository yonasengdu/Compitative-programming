class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_char = {}
        size_of_partions = []
        
        for ind in range(len(s)):
            end_char[s[ind]] = ind
        
        end = end_char[s[0]]
        size = 0
        
        for right in range(len(s)):
            end = max(end,end_char[s[right]])
            size += 1
            
            if right == end:

                size_of_partions.append(size)
                size = 0
            
            
                
        return size_of_partions
                
        