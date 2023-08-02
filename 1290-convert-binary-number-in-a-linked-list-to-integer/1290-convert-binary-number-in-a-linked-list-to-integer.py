# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length  = 0
        ans = 0
        prev  = head
        while prev.next:
            length += 1
            prev = prev.next
            
       
            
        while head:
            ans += (2**length * head.val)
            length -= 1
            head = head.next
            
        return ans
            
        
        