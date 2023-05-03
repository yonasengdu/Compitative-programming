# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node[0]:
                return 
            
            if node[2] and node[2].val % 2 == 0:
                self.ans += node[0].val
                
            dfs((node[0].left,node[0],node[1]))
            dfs((node[0].right,node[0],node[1]))
            
            
        dfs((root,None,None))
        
        return self.ans
        