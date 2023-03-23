# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        queue.append(root)
        if root:
            ans.append([root.val])
        while queue:
            level = []
            for node in queue:
                curr = node
                if curr:
                    level.append(curr.left)
                    level.append(curr.right)
                    
            queue = []      
            temp_ans = []
            for node in level:
                queue.append(node)
                
                if node:
                    temp_ans.append(node.val)
            if temp_ans:       
                ans.append(temp_ans)
                
                
                
          
            
        return ans