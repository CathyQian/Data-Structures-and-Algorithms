"""
Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.


"""

# dynamic programming

# solution 1, wrong
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0 # no refueling needed
        elif not stations:
            return -1 # no station but can't reach target without refueling
        
        stations = [[0, 0]] + stations # number of stations = stations index
        dp = [[-1, -1] for _ in range(len(stations))]
        dp[0] = [0, startFuel]
        for i in range(1, len(stations)):
            for j in range(i):
                if dp[j][0] != -1 and dp[j][1] + stations[j][0] >= stations[i][0]:
                    if (dp[i][0] != -1 and dp[i][0] > dp[j][0] + 1) or dp[i][0] == -1: # this condition does not consider reachability and thus wrong
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1] + stations[i][1] + stations[j][0] - stations[i][0]
            if dp[i][1] + stations[i][0] >= target: # can reach the target
                return dp[i][0] 
            if dp[i][0] == -1: # still can't reach station i
                return -1
        # if can't jump out of the for loop earlier --> cannot reach target
        return -1


# solution 2, correctm space complexity O(n2)
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        if not stations:
            if startFuel >= target:
                return 0
            else:
                return -1
        #dp[i], the farthest location we can get to using i refueling stops. 
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1): # i, i-1, .... 0, why backwards?
                if dp[t] >= location: # can reach station i
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: 
                return i
        return -1
    
# solution 3, heap
# When driving past a gas station, let's remember the amount of fuel it contained. We don't need to decide yet whether to fuel up here or not - 
# for example, there could be a bigger gas station up ahead that we would rather refuel at. 
# When we run out of fuel before reaching the next station, we'll retroactively fuel up: greedily choosing the largest gas stations first.
class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev # remaining fuel at this station
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq) # find the largest gas station to fuel
                ans += 1
            if tank < 0: 
                return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans

                  
                    