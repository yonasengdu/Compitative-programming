# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node,path_sum):
            if not node:
                return False
            
            
            path_sum = path_sum + node.val
            if not node.left and not node.right and path_sum == targetSum:
                return True
            
            
            return dfs(node.left,path_sum) or dfs(node.right,path_sum)
        
        
        return dfs(root,0)