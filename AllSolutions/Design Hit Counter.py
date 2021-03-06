"""
Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 

Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""

# space complexity O(N) -- N is number of hits, time complexity for hit is O(1) and getHit is O(N)
from collections import deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.hits:
            if self.hits[0] <= timestamp - 300:
                _ = self.hits.popleft()
            else:
                break
        return len(self.hits)

# follow up, scale up for large number of hits
# problem of the previous method is both time and space complexity goes up linearly with large number of hits
# per second

from collections import OrderedDict

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = 0 # number of hits in the past 5 min
        self.od = OrderedDict()  # timestamp: counts

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.c = self.getHits(timestamp)
        if timestamp not in self.od:
            self.od[timestamp] = 1
        else:
            self.od[timestamp] += 1
        self.c += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.od and next(iter(self.od)) <= timestamp - 300:
            self.c -= self.od.popitem(last=False)[1]
        return self.c