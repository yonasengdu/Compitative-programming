class MyStack:

    def __init__(self):
        self.item = []
    def push(self, x: int) -> None:
        return self.item.append(x)
    def pop(self) -> int:
        return self.item.pop()
    def top(self) -> int:
        return self.item[-1]
    def empty(self) -> bool:
        return self.item == []
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()