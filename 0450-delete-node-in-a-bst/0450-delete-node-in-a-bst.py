# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        
            if not root:
                    return root
            def find_min(node):
                current = node
                while current.left:
                    current = current.left
                return current  


        
        
            if key < root.val:
                root.left = self.deleteNode(root.left,key)
            elif key > root.val:
                root.right = self.deleteNode(root.right,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left



                temp = find_min(root.right)
                
                root.val = temp.val
                

                root.right = self.deleteNode(root.right,temp.val)

            return root
      