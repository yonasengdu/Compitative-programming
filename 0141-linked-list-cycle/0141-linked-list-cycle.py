# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()
        curr = head
        while curr:
            if curr in hash_set:
                return True
            hash_set.add(curr)
            curr = curr.next
        return False