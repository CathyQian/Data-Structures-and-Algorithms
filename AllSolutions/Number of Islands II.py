"""
Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]

Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0

Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

"""
# union find

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]: # m, n not needed
        self.parent, self.rank, self.count = {}, {}, 0
        return list(map(self.add, positions))   
    
    def find(self, x): # find root of x,point all nodes directly to the root --- called path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y): # every find or union operation will link node to the root of the set
        x, y = self.find(x), self.find(y)
        if x != y: # x, y not in the same set
            if self.rank[x] < self.rank[y]: # make sure self.rank[x] >= self.rank[y]
                x, y = y, x
            self.parent[y] = x # attach the shorter branch to the longer one
            if self.rank[x] == self.rank[y]: # union by rank
                self.rank[x] += 1
            self.count -= 1
            
    def add(self, pos): # can be added to the main function
        i, j = pos[0], pos[1]
        x = (i, j) # tuple can be key of dictionary, list can not.
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.count += 1
            for y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if y in self.parent:
                    self.union(x, y)
        return self.count

"""
disjoint-set

A disjoint-set forest consists of a number of elements each of which stores an id, a parent pointer, and, in 
efficient algorithms, either a size or a "rank" value. 

If a node's parent pointer is itself, it means this node is the root of the tree and is the representative member
of its set.

The MakeSet operation makes a new set by creating a new element with a unique id, a rank of 0, and a parent pointer
to itself. The parent pointer to itself indicates that the element is the representative member of its own set.

The MakeSet operation has O ( 1 ) {\displaystyle O(1)} O(1) time complexity, so initializing n sets has O(n) time 
complexity. 

Find(x) follows the chain of parent pointers from x up the tree until it reaches a root element, whose parent is 
itself. This root element is the representative member of the set to which x belongs, and may be x itself. 

Time complexity: 
If m operations, either Union or Find, are applied to n elements, the total run time is O(m log*n), where log* is the 
iterated logarithm.
For this specific problem, len(positions) = n, operations = O(n), time complexity O(nlog*n). Note that log*N is almost 
constant (for N = 265536, log*N = 5) in this universe, so the algorithm is almost linear with N.
"""

"""
Alternatively, the unionfind can be put in a separate class for future use.
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]: # m, n not needed
        res = []
        islands = UnionFind()
        for (i, j) in positions:
            x = (i, j) # tuple can be key of dictionary, list can not.
            if x not in islands.parent:
                # add node if it doesn't exist
                islands.parent[x] = x
                islands.rank[x] = 0
                islands.count += 1
                # union with neighbors if possible
                for y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if y in islands.parent:
                        islands.union(x, y)
            res.append(islands.count)
        return res   

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x): # find root of x,point all nodes directly to the root --- called path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y): # every find or union operation will link node to the root of the set
        x, y = self.find(x), self.find(y)
        if x != y: # x, y not in the same set
            if self.rank[x] < self.rank[y]: # make sure self.rank[x] >= self.rank[y]
                x, y = y, x
            self.parent[y] = x # attach the shorter branch to the longer one
            if self.rank[x] == self.rank[y]: # union by rank
                self.rank[x] += 1
            self.count -= 1
            
