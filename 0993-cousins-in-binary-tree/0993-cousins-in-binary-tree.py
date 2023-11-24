# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        
        queue = deque([(-1,root)])
        
        
        while queue:
            level_nodes = len(queue)
            par_x = None
            par_y = None
            
            for _ in range(level_nodes):
                par,curr_level_node = queue.popleft()
               
                
                if curr_level_node:
                    curr_node_val = curr_level_node.val
                    
                    queue.append((curr_level_node,curr_level_node.left))
                    queue.append((curr_level_node,curr_level_node.right))
                    
                    if curr_node_val == x:
                        par_x = par
                        
                    elif curr_node_val == y:
                        par_y = par
                        
          
            if par_x and par_y and par_x != par_y:
                return True
            
      
        return False
                    
                
            
        
        
        