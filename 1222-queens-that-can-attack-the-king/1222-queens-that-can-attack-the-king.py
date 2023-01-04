class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def find(row,col):
            new_king =king
            x,y = new_king
            ans =[]
            queen = set([tuple(queen) for queen in queens])
            while 0<= x and x <= 8 and 0<=y and y <= 8 :
                x += row
                y += col
                if (x,y) in queen: 
                    ans.append(x)
                    ans.append(y)
                    break
            if ans:
                return ans
            return 0
        dir = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        ans =[]
        for row,col in dir:
            temp_ans = find(row,col)
            if temp_ans:
                ans.append(temp_ans)
                
        return ans
            
