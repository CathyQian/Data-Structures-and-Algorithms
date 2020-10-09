"""
Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4


"""

"""
The tricky part is if you scan top to bottom and left to right, some cells will be populated earlier than the others, thus making the 
results of some cells wrong.
The right way is to start bfs or dfs from gates
"""

# right solution -- dfs
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        self.m, self.n = len(rooms), len(rooms[0])
        for i in range(self.m):
            for j in range(self.n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)
    
    def dfs(self, rooms, i, j, val):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or rooms[i][j] < val:
            return
        rooms[i][j] = val
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(rooms, i + x, j + y, val + 1)
        
# right solution, bfs (i like this better)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not len(rooms):
            return 
        
        q = []
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.pop(0)
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                if i+x < 0 or i+x >= m or j+y < 0 or j+y >= n or rooms[i+x][j+y] < rooms[i][j] + 1:
                    continue
                rooms[i+x][j+y] = rooms[i][j] + 1
                q.append((i+x, j+y))
