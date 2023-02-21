# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class List1:
    def __init__(self):
        self.head = None
        self.Tail = None
    def addAtTail(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.Tail = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            self.Tail = newNode
class List2:
    def __init__(self):
        self.head = None
    def addAtTail(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

                
        

    
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        list1= List1()
        list2 = List2()
        while curr:
            if curr.val < x:
                list1.addAtTail(curr.val)
            else:
                list2.addAtTail(curr.val)
            curr = curr.next
        if list1.Tail:
            list1.Tail.next = list2.head
            return list1.head
        return list2.head
                
             
                
                    
                