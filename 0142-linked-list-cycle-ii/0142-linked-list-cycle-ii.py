# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_set = set()
        curr = head
        while curr:
            if curr in hash_set:
                return curr
            hash_set.add(curr)
            curr = curr.next
        return None