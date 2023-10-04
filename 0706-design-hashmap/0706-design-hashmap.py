class MyHashMap:

    def __init__(self):
        self.map = [-1]*10
        

    def put(self, key: int, value: int) -> None: 
        if key >= len(self.map):
            self.map += [-1]* (key - len(self.map) + 1)
        self.map[key] = value
        

    def get(self, key: int) -> int:
        if key >= len(self.map) :
            return -1
        
        return self.map[key]
        

    def remove(self, key: int) -> None:
        if key < len(self.map):
             self.map[key] = -1
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)