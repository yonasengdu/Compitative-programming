# O(N*K) -- where N is the lenght of the list and K is the places
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #edge case empty list and list with only one element
        if not head or not head.next :
            return head
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        if k > length:
            
            num_rotation = k % length
        else:
            num_rotation = k
        
        
        
        
        #going for K times
        for ind in range(num_rotation):
            prev = head
            current = head.next
            
            #getting the last element in the list
            while current and current.next:
                prev = prev.next
                current = current.next
            prev.next = current.next
            temp = head
            head = current
            current.next = temp
        return head
            
                
            
            
        