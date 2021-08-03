"""
Bus Routes

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

"""

# typical bfs solution
from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # S: source, T: target
        # You already at the terminal, so you needn't take any bus.
        if S == T: return 0
        
        # You need to record all the buses you can take at each stop so that you can find out all
        # of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        stopBoard = {} 
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)
        
        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([(S, 0)])
        # Using visited to record the buses that have been taken before, because you needn't to take them again. Note not recorded stops
        visited = set()
        while queue:
            curStop, depth = queue.popleft()
            for bus in stopBoard[curStop]:
                # if the bus you have taken before, you needn't take it again.
                if bus in visited: 
                    continue
                visited.add(bus)
                for stop in routes[bus]:
                    if stop == T: 
                        return depth + 1
                    queue.append((stop, depth+1))
        return -1

