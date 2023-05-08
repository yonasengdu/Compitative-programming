# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        
        stack = deque()
        stack.append(root)
        
        while stack:
            curr = stack.popleft()
            
            if curr and curr.left:
                graph[curr.val].add(curr.left.val)
                graph[curr.left.val].add(curr.val)
                
            if curr and curr.right:
                graph[curr.val].add(curr.right.val)
                graph[curr.right.val].add(curr.val)
                
            if curr:    
                stack.append(curr.left)
                stack.append(curr.right)
                
                
        queue = deque()
        queue.append(target.val)
        ans = []
        visited = set([target.val])
       
        
      
        for _ in range(k):
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
               
                for node in graph[curr]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)

                    
                        
             
                        
                   
                        
                                
        return list(queue)
                        
                
            
            
            
            
     
                
        