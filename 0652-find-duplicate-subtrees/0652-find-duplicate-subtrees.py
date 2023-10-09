# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        
        def dfs(node):
            if not node:
                return "null"
            
            res =  ','.join([str(node.val),dfs(node.left),dfs(node.right)])
            
           
            if res in mapper and res not in visited:
                ans.append(mapper[res])
                visited.add(res)
                
            else:
                mapper[res] = node
                
            return res
        
        
        visited = set()
        mapper = {}
        ans = []
        dfs(root)
        
        return ans
        
        