# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        ans = []
        
        while queue:
            level_sum = 0
            levels = []
            c = 0
            for num in queue:
                level_sum += num.val
                c += 1

                if num.left:
                    levels.append(num.left)
                if num.right:
                    levels.append(num.right)

            avg = level_sum / c
            ans.append(avg)
           
        
            
            queue = levels
            
        return ans
            
            
            
          
                
            
        
        