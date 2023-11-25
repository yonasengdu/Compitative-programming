# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(1,root)])
        
        max_width = 0
        
        level = 1
        while queue:
            n = len(queue)
            start = (0,0)
            
            
            for _ in range(n):
                cur,node = queue.popleft()
                
                if not start[1] and node:
                    start = (cur,1)
                    
                 
                
                
                if node:
                    max_width = max(max_width,cur - start[0])
                    queue.append((cur * 2,node.left))
                    queue.append((cur*2 + 1, node.right))
                    
            level += 1
                    
                    
        return max_width + 1
                
        
        
        

            
                
                    
                
        