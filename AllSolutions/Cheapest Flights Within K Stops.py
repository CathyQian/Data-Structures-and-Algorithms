"""
Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst

"""

# solution 1: DFS, time exceed limit
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # represent directed graph with weights using adjacency dictionary
        graph = collections.defaultdict(dict)
        for flight in flights:
            start, end, price = flight[0], flight[1], flight[2]
            graph[start].update({end:price})

        # use DFS to do the search and find min price
        self.res = sys.maxsize
        self.dfs(graph, src, dst, k, -1, 0)
        return self.res if self.res != sys.maxsize else -1
    
    def dfs(self, graph, curstop, destination, k, numstops, curprice):
        if curstop == destination and numstops <= k:
            self.res = min(self.res, curprice)
        elif numstops < k and curprice < self.res:
            for nxtstop, price in graph[curstop].items():
                self.dfs(graph, nxtstop, destination, k, numstops + 1, curprice + price)
        return 
    
# solution 2: DFS + memo due to many duplicated steps

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        routes = collections.defaultdict(dict)
        for flight in flights:
            start, end, price = flight[0], flight[1], flight[2]
            routes[start].update({end:price})
        self.memo = {} # (city, residual stop): min distance to destination
        res = self.find_cost(routes, src, dst, K)

        return res if res != sys.maxsize else -1
    
    def find_cost(self, routes, city, dst, stop):
        if (city, stop) not in self.memo:
            res = sys.maxsize
            if city == dst: # at destination
                res = 0
            elif stop == 0: # directly linked to destination nonstop
                if city in routes and dst in routes[city]:
                    res = routes[city][dst]
            else:
                if city in routes:
                    for c in routes[city]:
                        res = min(res, routes[city][c] + self.find_cost(routes, c, dst, stop-1)) 
            self.memo[(city, stop)] = res

        return self.memo[(city, stop)]
        
# solution 4: BFS --- WRONG SOLUTION due to incorrect use of visited
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # directional graph with weight, use adj_list to represent
        adj_list = collections.defaultdict(dict)
        for flight in flights:
            start, end, cost = flight[0], flight[1], flight[2]
            adj_list[start].update({end: cost})
        # use BFS to traverse graph, # of layers max is k, record mincost along the way
        mincost = sys.maxsize
        q = collections.deque([(src, -1, 0)])
        visited = set([src])
        while q:
            station, numstops, cost = q.popleft()
            if station in adj_list:
                for sta, cst in adj_list[station].items():
                    if sta == dst and numstops < k:
                        mincost = min(mincost, cost + cst)
                    elif sta not in visited: # wrong, since new route may have shorter cost
                        q.append((sta, numstops + 1, cost + cst))
                        visited.add(sta)
        return mincost if mincost != sys.maxsize else -1

# solution 5: BFS --- VISITED leads to memory exceed limit if graph is too big
# ---> layer by layer scan (see solution 3)        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # directional graph with weight, use adj_list to represent
        adj_list = collections.defaultdict(dict)
        for flight in flights:
            start, end, cost = flight[0], flight[1], flight[2]
            adj_list[start].update({end: cost})
        # use BFS to traverse graph, # of layers max is k, record mincost along the way
        mincost = sys.maxsize
        q = collections.deque([(src, -1, 0)])
        visited = {(src, -1): 0}
        while q:
            station, numstops, cost = q.popleft()
            if station in adj_list:
                for sta, cst in adj_list[station].items():
                    if sta == dst and numstops < k:
                        mincost = min(mincost, cost + cst)
                    elif (sta, numstops +1) not in visited: # wrong, since new route may have shorter cost
                        q.append((sta, numstops + 1, cost + cst))
                        visited.update({(sta, numstops+1): cost + cst})
                    elif visited[(sta, numstops + 1)] > cost + cst:
                        q.append((sta, numstops + 1, cost + cst))
                        visited.update({(sta, numstops+1): cost + cst})

        return mincost if mincost != sys.maxsize else -1
    
# solution 6: BFS --- correct solution with min visited size    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # directional graph with weight, use adj_list to represent
        adj_list = collections.defaultdict(dict) # rename to routes??
        for flight in flights:
            start, end, cost = flight[0], flight[1], flight[2]
            adj_list[start].update({end: cost})
        # use BFS to traverse graph, # of layers max is k, record mincost along the way
        q = collections.deque([(src, -1, 0)])
        visited = [sys.maxsize] * n
        while q:
            station, numstops, cost = q.popleft()
            if station == dst or numstops == k:
                continue
            for nei, cst in adj_list[station].items():
                nei_cost = cost + cst 
                if nei_cost < visited[nei]:
                    visited[nei] = nei_cost
                    q.append((nei, numstops + 1, nei_cost))

        return visited[dst] if visited[dst] != sys.maxsize else -1