# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_twin_sum = 0
        n = 0
        
        curr = head 
        while curr:
            curr = curr.next
            n += 1
         
        prev = None
        curr = head
        for ind in range(n // 2):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while curr and prev:
            temp=[curr.val,prev.val]
            max_twin_sum = max(max_twin_sum,sum(temp))
            
            curr = curr.next
            prev = prev.next
            
            
        
        return max_twin_sum
            
            
            
            

                
            
            