# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        return nodes[len(nodes)//2]
     
            
            
        