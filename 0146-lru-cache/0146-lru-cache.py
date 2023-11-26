class Node:
    def __init__(self,val,key):
        self.prev = None
        self.next = None
    
    
        self.key = key
        self.val = val
    


class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity 
        self.cache = dict()
        
        
        self.head = Node(None,None)
        self.tail = Node(None,None)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        temp = node

        node.prev.next = node.next
        node.next.prev = node.prev
        
        temp.next = self.head.next
        self.head.next.prev = temp
        temp.prev = self.head
        self.head.next = temp
        
        
        
        
        return node.val

        

    def put(self, key: int, value: int) -> None:
     
        if key not in self.cache and len(self.cache) == self.capacity:
            temp =  self.tail.prev
            
            self.tail.prev = temp.prev
            temp.prev.next =  self.tail
            
            
            del self.cache[temp.key]
           
        
        
        if key not in self.cache:
            node = Node(value,key)
           
        else:
            node = self.cache[key]
            node.val = value
            temp = node
            
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        self.cache[key] = node

            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)