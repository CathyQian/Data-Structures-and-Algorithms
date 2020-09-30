"""
Network Delay Time

There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is 
the time it takes for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

"""
"""
# https://www.youtube.com/watch?v=vwLYDeghs_c (all three methods)
# https://www.youtube.com/watch?v=pVfj6mxhdMw (Dijkstra's method)
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

最短路径的常用解法有迪杰斯特拉算法 Dijkstra Algorithm, 弗洛伊德算法 Floyd-Warshall Algorithm, 和贝尔曼福特算法 Bellman-Ford Algorithm，其中，
Floyd 算法是多源最短路径，即求任意点到任意点到最短路径，而 Dijkstra 算法和 Bellman-Ford 算法是单源最短路径，即单个点到任意点到最短路径。这里因为
起点只有一个K，所以使用单源最短路径就行了。这三种算法还有一点不同，就是 Dijkstra 算法处理有向权重图时，权重必须为正，而另外两种可以处理负权重有向图，
但是不能出现负环，所谓负环，就是权重均为负的环。为啥呢，这里要先引入松弛操作 Relaxtion，这是这三个算法的核心思想，当有对边 (u, v) 是结点u到结点v，
如果 dist(v) > dist(u) + w(u, v)，那么 dist(v) 就可以被更新，这是所有这些的算法的核心操作。
"""

# Dijkstra's method
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

class Solution:    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:  
        dist = [sys.maxsize] * (N+1)
        dist[K] = 0
        visited = [False] * (N+1) 
        
        edges = {}
        for e in times:
            edges[(e[0], e[1])] = e[2]
            
        for node in range(N):
            
            # find min_indx u in unvisited set
            min = sys.maxsize
            for v in range(1+N):
                if dist[v] < min and visited[v] == False:
                    min = dist[v]
                    u = v
           
            visited[u] = True # add one node into visited each for loop
            for v in range(1, N+1): # search neighbor of v
                if (u, v) in edges and visited[v] == False and \
                     dist[v] > dist[u] + edges[(u,v)]: 
                    dist[v] = dist[u] + edges[(u,v)]
        res = 0            
        for i in range(1, N + 1):
            res = max(res, dist[i])

        return -1 if res == sys.maxsize else res
