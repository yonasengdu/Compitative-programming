# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        ans = []

        def inorder(root):
            nonlocal counter
            if root == None:
                return 
            
            inorder(root.left)
            counter[root.val] += 1
            inorder(root.right)
            
        inorder(root)
        
        rep = max([freq for freq in counter.values()])
        
        for val,freq in counter.items():
            if freq == rep:
                ans.append(val)
                
        return ans
    
        
       
        