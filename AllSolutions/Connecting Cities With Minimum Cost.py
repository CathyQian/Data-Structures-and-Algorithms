"""
Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those
 two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

Example 1:

Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:

Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.

 

Note:

    1 <= N <= 10000
    1 <= connections.length <= 10000
    1 <= connections[i][0], connections[i][1] <= N
    0 <= connections[i][2] <= 10^5
    connections[i][0] != connections[i][1]

"""

"""
注意：要找到的是所有可以将这些点连接在一起的路径中和最小的， 很容易理解错误。

MST（Minimum Spanning Tree，最小生成树）问题有两种通用的解法，Prim算法就是其中之一，它是从点的方面考虑构建一颗MST，大致思想是：设图G顶点集合为U，
首先任意选择图G中的一点作为起始点a，将该点加入集合V，再从集合U-V中找到另一点b使得点b到V中任意一点的权值最小，此时将b点也加入集合V；以此类推，现在的
集合V={a，b}，再从集合U-V中找到另一点c使得点c到V中任意一点的权值最小，此时将c点加入集合V，直至所有顶点全部被加入V，此时就构建出了一颗MST。因为有N
个顶点，所以该MST就有N-1条边，每一次向集合V中加入一个点，就意味着找到一条MST的边。

Kruskal算法是基于贪心的思想得到的。首先我们把所有的边按照权值先从小到大排列，接着按照顺序选取每条边，如果这条边的两个端点不属于同一集合，那么就将它
们合并，直到所有的点都属于同一个集合为止。至于怎么合并到一个集合，那么这里我们就可以用到一个工具——-并查集。换而言之，Kruskal算法就是基于并查集的贪
心算法。
"""

# Krusakl method -- union find
# Time Complexity: O(mlogm + mlog*N). sort takes O(mlogm). find takes O(mlog*N)
Statement: If m operations, either Union or Find, are applied to n elements, the total run time is O(m log*n), where log* is the iterated logarithm. 
# Space: O(N)
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int: 
        self.part = N
        self.parent = {i:i for i in range(N)}
       
        self.res = 0
        for conn in sorted(connections, key=lambda x: x[2]):
            a, b, cost = conn[0] - 1, conn[1] - 1, conn[2]
            self.union(a, b, cost)
            if self.part == 1:
                return self.res
        return -1

    def find(self, a: int) -> int:
        if self.parent[a] == a:
            return a
        return self.find(self.parent[a])

    def union(self, a: int, b: int, cost: int) -> None:
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pa] = pb
            self.part -= 1
            self.res += cost
        