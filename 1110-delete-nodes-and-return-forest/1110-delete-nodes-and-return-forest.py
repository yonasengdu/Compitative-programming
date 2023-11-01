# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node,par,dirction):
            if not node:
                return 
            
            dfs(node.left,node,"l")
            dfs(node.right,node,"r")
            
            if node.val in to_delete:
                
                if node.left:
                    ans.append(node.left)
                    
                if node.right:
                    ans.append(node.right)
                
                if dirction == 'l':
                    par.left = None
                    
                elif dirction == 'r':
                    par.right = None
            
                    
        to_delete = set(to_delete)
        
      
        ans = []
        if root.val not in to_delete:
            ans.append(root)
            
        dfs(root,-1,-1)
       
        
        
        return ans
        
            
            
        
    
        
        