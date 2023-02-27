class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0]*(n+1) for i in range(n+1)]
        for query in queries:
            row_start = query[0]
            col_start = query[1]
            row_end = query[2]
            col_end = query[3]
            
            arr[row_start][col_start] += 1
            arr[row_start][col_end + 1] += -1
            arr[row_end + 1][col_start] += -1
            arr[row_end + 1][col_end + 1] += 1
            
        arr.append([0]*(n+1))    
        for row in arr:
            row.append(0)
        
                
        for row in range(n+1):
            for col in range(n+1):
                arr[row][col] += arr[row - 1][col] + arr[row][col - 1] - arr[row - 1][col - 1]
                
        for row in arr:
            row.pop()
            row.pop()
        arr.pop()
        arr.pop()
        
        return arr
        
        
            
            
            
        