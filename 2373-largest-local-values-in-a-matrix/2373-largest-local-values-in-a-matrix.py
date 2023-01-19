class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        start = 0
        end = 3
        ans =[]
        while end <= len(grid):
            temp_ans = []
            temp_mat = grid[start:end]
            
            s=0
            e=3
            while e <= len(grid):
                maximum = 0
                for row in temp_mat:
                    temp = row[s:e]
                    if max(temp) >= maximum:
                        maximum = max(temp)
                temp_ans.append(maximum)
         
                s+=1
                e+=1
            start+=1
            end+=1 
            ans.append(temp_ans)
        return ans
       
            
                
                
        