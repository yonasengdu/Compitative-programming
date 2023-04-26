# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
           
        if not root:
            return []
        
        
        queue = [root]
        ans = []
     
        
        while queue:
            levels = []
            nums = []
            for num in queue:
                nums.append(num.val)
              

                if num.left:
                    levels.append(num.left)
                if num.right:
                    levels.append(num.right)
                    
            ans.append(nums)
                    
            
            
            queue = levels
        
        return  ans[::-1]
            
        