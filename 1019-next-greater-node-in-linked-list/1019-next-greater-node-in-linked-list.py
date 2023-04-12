# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        new_list = head
        nums  = []
        while new_list:
            nums.append(new_list.val)
            new_list = new_list.next
            
        monotone = []
        ans = [0]*len(nums)
        for i in range(len(nums)):
            while  monotone and nums[monotone[-1]] < nums[i]:
                ans[monotone[-1]] = nums[i]
                monotone.pop()
                
            monotone.append(i)
       
        return ans
                    
                
        
 
        