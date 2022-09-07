class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.item = []
    def insertFront(self, value: int) -> bool:
             if len(self.item)<self.k:
                self.item.insert(0,value)
                return True
             else:return False
    def insertLast(self, value: int) -> bool:
             if len(self.item)<self.k:
                self.item.append(value)
                return True
             else: return False
    def deleteFront(self) -> bool:
             if len(self.item)>0:
                self.item.pop(0)
                return True
             else: return False
    def deleteLast(self) -> bool:
             if len(self.item)>0:
                self.item.pop()
                return True
             else: return False
    def getFront(self) -> int:
             if len(self.item)==0:
                return -1
             else: return self.item[0]
    def getRear(self) -> int:
             if len(self.item)==0:
                return -1
             else: return self.item[-1]
    def isEmpty(self) -> bool:
             return self.item == []
    def isFull(self) -> bool:
        return len(self.item)==self.k
                     
                


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()