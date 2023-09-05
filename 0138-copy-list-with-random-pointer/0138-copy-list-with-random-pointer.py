"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = {}
        
        
        
        curr = head
        
        while curr:
            copy_dict[curr] = Node(curr.val)
            curr = curr.next
            
        for node,cp in copy_dict.items():
            
            if node.next:
                cp.next = copy_dict[node.next]
                
            if node.random:
                cp.random =  copy_dict[node.random]
            
            
           
                                
        
        return copy_dict[head] if head else None
       
        