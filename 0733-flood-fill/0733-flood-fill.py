class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.orignal = image[sr][sc]
        def is_valid(row,col):
            return (0 <= row < len(image)) and (0 <= col < len(image[0])) and (image[row][col] == self.orignal) and (image[row][col] != color)
        
        def dfs(row,col):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            image[row][col] = color

            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if is_valid(new_row,new_col):
                    dfs(new_row,new_col)
        dfs(sr,sc)        
        return image
                
        
        
        