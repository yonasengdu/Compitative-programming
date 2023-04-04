# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        
        def helper(node,curr):
            if not node:
                return
            helper(node.left,curr+node.val)
            helper(node.right,curr+node.val)
            
            if curr + node.val == targetSum:
                self.count += 1
                
        def dfs(root):
            if root == None:
                return []
            helper(root,0)
            left = dfs(root.left)
            right = dfs(root.right)
            
           
          
        
        
        dfs(root)
        return self.count
            
        