# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        
        def dfs(node):
            if not node:
                return None
            
            
            left = dfs(node.left)
            right = dfs(node.right)
         
            if not left and not right:
                self.res = max(self.res,node.val)
                return node.val 
                    
            if not right:
                
                sub_path_sum =  left + node.val
                self.res = max(left,sub_path_sum,self.res,node.val)
                return node.val + max(left,0)
                
            if not left:
                sub_path_sum = right + node.val
                self.res = max(right,sub_path_sum,self.res,node.val)
                return node.val + max(right,0)
            
            sub_path_sum = right + left + node.val
            self.res = max(right,left,sub_path_sum,self.res,node.val,node.val + max(left,right,0))
            
            return node.val + max(left,right,0)
          
            
           
        
        dfs(root)
        
        return self.res
            
                