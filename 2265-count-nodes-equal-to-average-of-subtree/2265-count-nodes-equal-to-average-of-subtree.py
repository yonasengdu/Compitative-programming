# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode],ans=0) -> int:
        count = 0
        
        def calculate(root):
            nonlocal count
            if root == None:
                return (0, 0)
                
            
            
            
            left = calculate(root.left)
            right = calculate(root.right)
           
            magic = (root.val + left[0] + right[0], right[1] + left[1] +  1)
            
            if magic[0] // magic[1] == root.val:
                count += 1
            
            return  magic
        
        calculate(root)
        return count
        
      
            
        
        