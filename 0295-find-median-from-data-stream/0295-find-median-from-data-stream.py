from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.dataStream = SortedList()
    
        

    def addNum(self, num: int) -> None:
        self.dataStream.add(num)
        

    def findMedian(self) -> float:
        n = len(self.dataStream)
        if n  % 2 != 0:
            return self.dataStream[n // 2]
        else:
            return (self.dataStream[n // 2] + self.dataStream[(n // 2) - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()