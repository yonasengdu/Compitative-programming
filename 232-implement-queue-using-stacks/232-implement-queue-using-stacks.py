class MyQueue:

    def __init__(self):
        self.item=[]
        
    def push(self, x: int) -> None:
        return self.item.append(x)
        
    def pop(self) -> int:
        return self.item.pop(0)
        
    def peek(self) -> int:
        return self.item[0]

    def empty(self) -> bool:
        return self.item == []
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()