class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        
        diagonals_collection = defaultdict(list)
        
        
        for row_idx,row in enumerate(nums):
            for col_idx,_ in enumerate(row):
                diagonals_collection[(row_idx + col_idx)].append(nums[row_idx][col_idx])
                
        
        diagonals = []  
        max_idx_sum = max(diagonals_collection.keys())
            
        for idx_sum in range(max_idx_sum + 1):
            sub_diagonals = diagonals_collection[idx_sum]
            diagonals += sub_diagonals[::-1]
            
        return diagonals
    
            
            
        
                
        
    
        
        
        
        
        
        
        
        