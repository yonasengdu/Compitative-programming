"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 0
        def dfs(root,count=0):
            if not root.children:
                self.ans = max(self.ans,count+1)
                return 
            
            for child in root.children:
                dfs(child,count+1)
        if root:
            dfs(root)
        return self.ans