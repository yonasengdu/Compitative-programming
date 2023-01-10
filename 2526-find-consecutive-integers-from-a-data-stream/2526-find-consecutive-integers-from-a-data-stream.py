class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        self.ptr = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if self.stream[-1] != self.value:
            self.ptr = len(self.stream)
       
        diff = abs(len(self.stream)-self.ptr)
        if diff >= self.k:
            return True
        else: 
            return False
            
            
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)