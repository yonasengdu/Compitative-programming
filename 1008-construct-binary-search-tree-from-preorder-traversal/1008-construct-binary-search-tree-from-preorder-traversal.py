# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        mybst = TreeNode(preorder[0])
        
        def find_place(tree ,node):
            if not tree:
                return
            
            if tree.val < node.val:
                if not tree.right:
                    tree.right = node
                find_place(tree.right,node)
            elif tree.val > node.val:
                if not tree.left:
                    tree.left = node
                find_place(tree.left,node)
                
        for ind in range(1,len(preorder)):
            node = TreeNode(preorder[ind])
            find_place(mybst,node)
            
            
        return mybst
                
                