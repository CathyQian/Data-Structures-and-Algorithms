"""
Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.maxsize = size
        self.elements = []
        self.cursum = 0

    def next(self, val: int) -> float:
        curlen = len(self.elements)
        if curlen < self.maxsize:
            self.elements.append(val)
            self.cursum += val
            avg = self.cursum/(curlen + 1)
        else:
            old = self.elements.pop(0)
            self.elements.append(val)
            self.cursum = self.cursum - old + val
            avg = self.cursum/curlen
        return avg
    
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)