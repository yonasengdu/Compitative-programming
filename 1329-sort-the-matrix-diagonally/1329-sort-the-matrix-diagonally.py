class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        for col in range(len(mat[0])):
            gather = []
            
            temp = (0,col)
            while 0 <= temp[0] < len(mat) and 0 <= temp[1] < len(mat[0]):
                gather.append(mat[temp[0]][temp[1]])
                temp = (temp[0] + 1,temp[1] + 1)
                
                
            gather.sort()
            temp = (0,col)
            for i in range(len(gather)):
                mat[temp[0]][temp[1]] = gather[i]
                temp = (temp[0] + 1,temp[1] + 1)
                
                
                
                
        for row in range(1,len(mat)):
            gather = []
            
            temp = (row,0)
            while 0 <= temp[0] < len(mat) and 0 <= temp[1] < len(mat[0]):
                gather.append(mat[temp[0]][temp[1]])
                temp = (temp[0] + 1,temp[1] + 1)
                
                
            gather.sort()
            
            temp = (row,0)
            for i in range(len(gather)):
                mat[temp[0]][temp[1]] = gather[i]
                temp = (temp[0] + 1,temp[1] + 1)
                
        return mat
                
                
                
        
        
        
        
        