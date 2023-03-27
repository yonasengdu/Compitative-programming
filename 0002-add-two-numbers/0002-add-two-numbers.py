# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        rem = 0
            
        def calculate_num(left=ListNode(),right=ListNode()):
            nonlocal rem
            curr_sum = left.val + right.val + rem
            rem = 0
            checker =  str(curr_sum)
            num = int(checker[-1])
            
            if len(checker) > 1:
                rem = int(checker[0])
                
            return num
    

        while left and right:
            left.val = calculate_num(left,right)

            left = left.next
            right = right.next


        if right:
            temp = l1
            while temp.next:
                temp = temp.next
                
            temp.next = right
            left = temp.next
            
       
        while left:
            left.val = calculate_num(left)
            left = left.next

          
        if rem:
            temp = l1
            while temp.next:
                temp = temp.next
                
            temp.next = ListNode(rem)
                
           
            
    
        return l1
            
                

        