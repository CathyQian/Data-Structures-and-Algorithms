"""
Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

    Each 0 marks an empty land which you can pass by freely.
    Each 1 marks a building which you cannot pass through.
    Each 2 marks an obstacle which you cannot pass through.

Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

"""

# use bfs to calculate distance from each building to each empty place, use self.all_sum to store incremental values
# then get min(self.all_sum)
import collections, sys
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:         
        m,n = len(grid),len(grid[0])
        self.all_sum = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j) # find shortest distance from building to all empty cells
        min_dist = sys.maxsize
        for i in range(m):# cannot be replaced by min(self.all_sum), will return a list instead of an integer
            for j in range(n):
                if grid[i][j] == 0:
                    min_dist = min(min_dist, self.all_sum[i][j])
        
        return min_dist if min_dist != sys.maxsize else -1
    
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        distance = [[sys.maxsize]*n for _ in range(m)]
        q = collections.deque()
        q.append((i,j,0))
        
        while q:
            i, j, dist = q.popleft()
            for x, y in [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]:
                if 0<=x<m and 0<=y<n and grid[x][y] == 0:
                    if distance[x][y] > dist+1: # update distance
                        distance[x][y] = dist+1
                        q.append((x,y,distance[x][y]))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.all_sum[i][j] += distance[i][j]
        return distance