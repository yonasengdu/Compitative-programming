# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head
        second = head
        middle = first.next
        for ind in range(2):
            if second:
                second = second.next
        while second :
            secondNext = second.next
            firstNext = first.next
            
            first.next = second
            second.next = firstNext
            middle.next = secondNext
            
            first = first.next
            middle = middle.next
            
            if secondNext:
                second = secondNext.next
            else:
                break
        return head
        