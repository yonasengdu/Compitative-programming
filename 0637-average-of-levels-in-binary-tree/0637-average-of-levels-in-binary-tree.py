# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        
        average = []
        
        
        while queue:
            level_size = len(queue)
            total = 0
            for _ in range(level_size):
                current = queue.popleft()
                total += current.val
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            avg = total / level_size
            
            average.append(avg)
            
        return average
                
     
            
          
                
            
        
        