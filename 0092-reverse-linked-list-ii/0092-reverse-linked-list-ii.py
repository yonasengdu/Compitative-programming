# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left_prev = dummy #after both first_step and second_step this holdes the node before the left pointer
        current = head #after second_step this holds the node after the right pointer
        
        prev = None
        
        #reach the node at the left index
        
        for ind in range(left -1): #first_step
            left_prev, current = current , current.next
        
        #reverse the nodes between left and right
        for ind in range(right - left + 1): # second_step
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        #just simple re-arrengement
        left_prev.next.next = current
        left_prev.next = prev
        return dummy.next
        
            
         
 
        
 