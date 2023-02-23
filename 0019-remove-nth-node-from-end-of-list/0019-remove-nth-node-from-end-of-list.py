# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        current = head
        # print(length)
        if length == n:
            head = current.next
        else:
            steps = length - n-1
            for step in range(steps):
                current = current.next
            current.next = current.next.next
        return head
            
            
        
            
        
        