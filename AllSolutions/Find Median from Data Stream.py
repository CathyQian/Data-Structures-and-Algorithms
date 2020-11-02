"""
Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

 

Follow up:

    If all integer numbers from the stream are between 0 and 100, how would you optimize it?
    If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


"""
# small里存的更大的那一半，large存的是较小的那一半
from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_max = []
        self.heap_min = []
        

    def addNum(self, num: int) -> None:
        if not self.heap_max or num < -self.heap_max[0]:
            heappush(self.heap_max, -num)
        else:
            heappush(self.heap_min, num)
            
        if len(self.heap_max) - len(self.heap_min) > 1:
            heappush(self.heap_min, -heappop(self.heap_max))
        elif len(self.heap_min) - len(self.heap_max) > 0:
            heappush(self.heap_max, -heappop(self.heap_min))
            
        

    def findMedian(self) -> float:
        if len(self.heap_min) == len(self.heap_max):
            return (self.heap_min[0] - self.heap_max[0])/2
        else:
            return -self.heap_max[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""
Follow up:

1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?

We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.

Time and space complexity would be O(100) = O(1).

2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

As 99% is between 0-100. So can keep a counter for less_than_hundred and greater_than_hundred.
As we know soluiton will be definately in 0-100 we don't need to know those number which are >100 or <0, only count of them will be enough.
"""