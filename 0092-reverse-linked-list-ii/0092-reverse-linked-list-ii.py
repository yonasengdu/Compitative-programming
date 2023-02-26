# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left_prev = dummy
        current = head
        
        prev = None
        for ind in range(left -1):
            left_prev, current = current , current.next
        
        for ind in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        left_prev.next.next = current
        left_prev.next = prev
        return dummy.next
        
            
         
 
        
 