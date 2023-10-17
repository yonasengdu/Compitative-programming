# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        curr =  l1
        while curr:
            num1.append(str(curr.val))
            curr = curr.next
            
        curr = l2
        while curr:
            num2.append(str(curr.val))
            curr = curr.next
            
        ans = int(''.join(num1)) + int(''.join(num2))
        
        dummy = ListNode()
        
        curr = dummy
        
        for num in str(ans):
            temp = ListNode(int(num))
            curr.next = temp 
            curr = curr.next
            
        return dummy.next
            
        
        
        
        