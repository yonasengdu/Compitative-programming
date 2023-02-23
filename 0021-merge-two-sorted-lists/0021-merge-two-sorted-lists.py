# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SortedList:
    def __init__(self):
        self.head = None
    def addAtTail(self,val):
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = SortedList()
        while list1 and list2:
            if list1.val == list2.val:
                newList.addAtTail(list1.val)
                newList.addAtTail(list1.val)
                list1 = list1.next
                list2 = list2.next
            elif list1.val > list2.val:
                newList.addAtTail(list2.val)
                list2 = list2.next
            else:
                newList.addAtTail(list1.val)
                list1 = list1.next
        while list1:
            newList.addAtTail(list1.val)
            list1 = list1.next
        while list2:
            newList.addAtTail(list2.val)
            list2 = list2.next
        return newList.head
                
                
                

                