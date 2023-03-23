# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = [root]
        
        if root:
            ans.append(root.val)
        while queue:
            level = []
            
            for node in queue:
                
                if node and node.left:
                    level.append(node.left)
                if node and node.right:
                    level.append(node.right)
                    
            queue = []
            if level:
                ans.append(level[-1].val)
            
            for node in level:
                queue.append(node)
                
        return ans
            
        