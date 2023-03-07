# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def find_max(root):
            if not root:
                return 0
            left = 1 + find_max(root.left)
            right = 1 + find_max(root.right)
            
            return max(left,right)
        return find_max(root)

        