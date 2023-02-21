# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def traversAnddCheck(left,right):
    while left and right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    if not left and not right:
        return True
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
       
        while curr:
            count += 1
            curr = curr.next
        
        prev = None
        curr = head
        if count % 2 == 0 :
            for i in range(count//2):
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
        else:
            for i in range(count//2):
               
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr= temp
            curr = curr.next
        return traversAnddCheck(prev,curr)
       
            
            
            
                    
                
                
        
        