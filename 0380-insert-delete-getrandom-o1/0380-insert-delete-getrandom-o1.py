class RandomizedSet:

    def __init__(self):
        self.theIdx = {}
        self.theArr = []
      
        

    def insert(self, val: int) -> bool:
        if val not in self.theIdx:
            self.theArr.append(val)
            self.theIdx[val] = len(self.theArr) - 1
            return True
        
       
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.theIdx:
            idx = self.theIdx[val]
           
            n = len(self.theArr)

            temp = self.theArr[idx]
            self.theArr[idx] = self.theArr[n-1]
            self.theArr[n-1] = temp
            
            self.theIdx[self.theArr[idx]] = idx
            self.theArr.pop()
            del self.theIdx[val]
            return True
        return False
        
        

    def getRandom(self) -> int:
        rand = random.choice(self.theArr)
       
        return rand
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()