class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        self.pairs = 0
        
        def divide(low,high):
            
            
            if low == high:
                return [nums[low]]
         
            
            mid = (high + low) // 2
            
            
            left = divide(low,mid)
            right = divide(mid + 1 ,high)
            
            
         
            
            left_pt = 0
            right_pt = 0
            
            merged = []
            
            while left_pt < len(left) and right_pt < len(right):
                if left[left_pt] <right[right_pt]:
                    merged.append(left[left_pt])
                    left_pt += 1
                    
                elif left[left_pt]  > right[right_pt]:
                    merged.append(right[right_pt])
                    right_pt += 1
                    
                else:
                    merged.append(left[left_pt])
                    merged.append(right[right_pt])
                    left_pt += 1
                    right_pt += 1
                           
            merged.extend(left[left_pt:])
            merged.extend(right[right_pt:])
            
            left_pt = 0
            right_pt = 0
            
            for left_num in left:
                while right_pt < len(right) and left_num > 2 * right[right_pt]:
                    right_pt += 1
                    
                self.pairs += right_pt
            
            
            
            return merged
        
        divide(0,len(nums) - 1)
        
        return self.pairs
        
        
            
            
        
            
            
                    
            
            
            
            
        