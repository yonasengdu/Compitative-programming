# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.summ = 0
        def dfs(node,number):
            if node == None:
                return
            if node and not node.left and not node.right:
                number.append(str(node.val))
                num = int("".join(number))
                self.summ += num
           
                return
            
            children = [node.left,node.right]
            
            for child in children:
                dfs(child,number + [str(node.val)])
            
            return
            
            
  
        
        dfs(root,[])
        
        return self.summ 
    
        