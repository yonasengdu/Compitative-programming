# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         n = len(grid)
        
#         uf = [[(j,i) for i in range(n)] for j in range(n)]
#         rank = [[1 for i in range(n)] for j in range(n)]
        
        
        
#         def inbound(node):
#             return 0 <=  node[0] < n and 0 <= node[1] < n
        
#         def find(node):
            
#             if node == uf[node[0]][node[1]]:
#                 return node
            
#             uf[node[0]][node[1]] = find(uf[node[0]][node[1]])
            
#             return uf[node[0]][node[1]]
        
        
        
#         def union(node1,node2):
#             par1 = find(node1)
#             par2 = find(node2)
#             if par1 == par2:
#                 return
            
#             if rank[par1[0]][par1[1]] >= rank[par2[0]][par2[1]]:
                
#                 uf[par2[0]][par2[0]] = par1
#                 rank[par1[0]][par1[1]] += rank[par2[0]][par2[1]]
#                 rank[par2[0]][par2[1]] = 0
             
                
#             else:
                
#                 uf[par1[0]][par1[0]] = par2
#                 rank[par2[0]][par2[1]] += rank[par1[0]][par1[1]]
#                 rank[par1[0]][par1[1]] = 0
             
                
                
                
#         def bfs(node):
#             row,col = node
#             direction = [(0,1),(1,0),(0,-1),(-1,0)]
#             pars = set()
#             size = 0
            
#             for row_shift, col_shift in direction:
#                 nei = (row + row_shift,col + col_shift)
                
#                 if inbound(nei):
#                     nei_par = find(nei)
#                     pars.add(nei_par)
                
#             for par in pars:
#                 par_row,par_col = par
#                 par_size = rank[par_row][par_col]
#                 size += par_size
                
#             return size + 1
        
#         def dfs(node):
#             row,col = node
#             direction = [(0,1),(1,0),(0,-1),(-1,0)]
            
#             for row_shift, col_shift in direction:
#                 nei = (row + row_shift,col + col_shift)
                
#                 if nei not in visited and inbound(nei) and grid[nei[0]][nei[1]]:
#                     nei_par = union(nei,head)
#                     visited.add(nei)
#                     dfs(nei)
                  
#         largeIsland = 0         
#         for row in range(n):
#             for col in range(n):
#                 if grid[row][col] == 1:
#                     head = (row,col)
#                     visited = set()
#                     dfs(head)
#                     largeIsland = max(largeIsland,rank[row][col])
                    
                    
                      
         
        # for row in range(n):
#             for col in range(n):
#                 if grid[row][col] == 0:
#                     node = (row,col)
#                     largeIsland = max(largeIsland,bfs(node))
                    
#         return largeIsland
                    
                    
                
            
                
            
            
     
        
class UnionFind():
    def __init__(self,n) -> None:
        self.root = {} 
        self.rank = defaultdict(lambda:1)
        
        for i in range(n):
            for j in range(n):
                self.root[(i,j)] = (i,j)
 

    def find(self, x):
        if self.root[x]  != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        repX = self.find(x)
        repY = self.find(y)
        
        if repX == repY:
            return 
        
        if self.rank[repX] <= self.rank[repY]:
            self.root[repX]  = repY
            self.rank[repY] += self.rank[repX]
            
        else:
            self.root[repY] = repX
            self.rank[repX] += self.rank[repY]
        
            
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)     
        uf = UnionFind(n)
        def inbound(node):
            return 0 <=  node[0] < n and 0 <= node[1] < n         
                
        def bfs(node):
            row,col = node
            direction = [(0,1),(1,0),(0,-1),(-1,0)]
            pars = set()
            size = 0
            
            for row_shift, col_shift in direction:
                nei = (row + row_shift,col + col_shift) 
                if inbound(nei) and grid[nei[0]][nei[1]]:
                    nei_par = uf.find(nei)
                    pars.add(nei_par)
                
            
            for par in pars: 
                par_size = uf.rank[par]
                size += par_size
                
            return size + 1
        
        def dfs(node):
            row,col = node
            direction = [(0,1),(1,0),(0,-1),(-1,0)]
            
            for row_shift, col_shift in direction:
                nei = (row + row_shift,col + col_shift)
                
                if  inbound(nei) and grid[nei[0]][nei[1]]:
                    nei_par = uf.union(nei,node)
                    
                   
               
                  
          
        for row in range(n):
            for col in range(n):
                uf.find((row,col))
                        
        largeIsland = 1
       
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    head = (row,col)
                    visited = set()
                    dfs(head)
                    
                    
                    
             
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    node = (row,col)
                    largeIsland = max(largeIsland,bfs(node))
                    
                    
        if largeIsland == 1 and grid[0][0] == 1:
            return n*n
                    
        return largeIsland
                    
                    
                