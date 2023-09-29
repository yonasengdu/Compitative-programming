class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda:TrieNode())
        self.Map = 0
        self.end = False
        

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(str)
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            curr = curr.children[char]
            if key in self.map:
                curr.Map += val - self.map[key]
            else:
                curr.Map += val
        
        self.map[key] = val
        curr.End = False        

    def sum(self, prefix: str) -> int:
        curr = self.root
        tally = 0
        for char in prefix:
            curr = curr.children[char]
        
        tally += curr.Map
        
        return tally
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)