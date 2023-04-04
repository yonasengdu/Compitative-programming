# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        if not root:
            return self.paths
        
        def dfs(root, curr):
            if not root:   
                return
            
            curr.append(root.val)
            if not root.left and not root.right:
                if sum(curr) == targetSum:
                    self.paths.append(curr[:])

          
            dfs(root.left,curr)
            dfs(root.right,curr)
            curr.pop()
        dfs(root,[])
        return self.paths
            
        