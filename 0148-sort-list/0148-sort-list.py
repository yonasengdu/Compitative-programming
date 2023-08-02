# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        prev = head
        while prev:
            values.append(prev.val)
            prev = prev.next
            
        values.sort()
        
        dummy = ListNode()
        curr = dummy
        for val in values:
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next
            
        return dummy.next
            
        