# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        ctr = 0
        
        while temp:
            ctr += 1
            temp = temp.next
            
        mod = ctr % k   if k <= ctr else 0
        div = ctr // k
     
       
        ans = []
        
        temp2 = head
        
        while temp2:  
            
            curr_temp = temp2
            for i in range(div - 1):
                if temp2:
                    temp2 = temp2.next
                
            if mod and temp2:
                mod -= 1
                temp2 = temp2.next
               
            if temp2:
                fun_temp = temp2.next
                temp2.next = None
                
                temp2 = fun_temp
                
            
                
            ans.append(curr_temp)
            
        for left in range(k - len(ans)):
            ans.append(None)
            
           
                    
            
                    
            
          
                
            
        return ans
            
            
        